from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255)
    picture = models.URLField()
    description = models.TextField()
