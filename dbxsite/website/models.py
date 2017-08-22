from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    tags = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=32, null=True)
    publish_time = models.DateTimeField(auto_now_add=True)
