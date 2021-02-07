import os
import string

from django.db import models
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from martor.models import MartorField


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Intel(models.Model):
    RESOURCE_TYPE_CHOICES= (
        ('article', 'Article'),
        ('book', 'Book'),
        ('text', 'Text'),
        ('tool', 'Tool'),
    )

    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, related_name='intels', null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1500, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)

    tags = models.ManyToManyField(Tag, related_name='intels')

    link = models.URLField(blank=True)
    text_content = MartorField(blank=True)
    additional_note = models.TextField(max_length=3000, blank=True)

    def __str__(self):
        return "#%s - %s" % (self.id, self.title)


def get_upload_path(instance, filename):
    base_filename, ext = os.path.splitext(filename)
    # len(charset) ** n = 62**6=5e10
    rdm = get_random_string(length=6, allowed_chars=string.ascii_letters+string.digits)
    new_filename = f'{base_filename}_{rdm}{ext}'
    return os.path.join("intel_files", "intel_%d" % instance.intel.id, new_filename)


class IntelFile(models.Model):
    intel = models.ForeignKey(Intel, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=get_upload_path)
    link = models.URLField(blank=True)

    def filename(self):
        return os.path.basename(self.file.name)


# These two auto-delete files from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=IntelFile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem when corresponding `IntelFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            instance.file.delete(save=False)


@receiver(models.signals.pre_save, sender=IntelFile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem when corresponding `IntelFile` object is updated with new file.
    """
    if not instance.pk:
        return False
    try:
        old_file = IntelFile.objects.get(pk=instance.pk).file
    except IntelFile.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            instance.file.delete(save=False)
