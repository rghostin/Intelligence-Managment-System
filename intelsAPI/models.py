import os

from django.db import models
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
    return os.path.join("intel_files", "intel_%d" % instance.intel.id, filename)


class IntelFile(models.Model):
    intel = models.ForeignKey(Intel, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=get_upload_path)

    def filename(self):
        return os.path.basename(self.file.name)



