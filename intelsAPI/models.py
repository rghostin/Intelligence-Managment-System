from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Intel(models.Model):
    RESOURCE_TYPE_CHOICES= (
        ('article', 'Article'),
        ('book', 'Book'),
        ('text', 'Text'),
    )

    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, related_name='intels', null=True)
    title = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)

    tags = models.ManyToManyField(Tag, related_name='intels')

    link = models.URLField(blank=True)
    text_content = models.TextField(max_length=10000, blank=True)
    additional_note = models.TextField(max_length=3000, blank=True)


# class IntelFile:
#     intel = models.ForeignKey(Intel, on_delete=models.CASCADE, related_name='files')
#     file = models.FileField(upload_to="resources/")


