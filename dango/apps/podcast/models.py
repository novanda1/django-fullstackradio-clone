from django.db import models
# from ckeditor.fields import RichTextField
from cms.models.fields import PlaceholderField


class Host(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


STATUS_CHOICES = (
    (0, 'draft'),
    (1, 'publish')
)


class Episode(models.Model):
    host = models.ForeignKey(
        Host, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    title = models.CharField(max_length=200)
    podcast = models.CharField(max_length=200, null=True, blank=True)
    content = PlaceholderField(
        'podcast_content', related_name='podcast_content')
    excerpt = models.TextField(default="excerpt")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
