from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='标题')
    content = models.TextField(null=True, verbose_name='内容')
    tags = models.CharField(max_length=100, null=True, verbose_name='标签')
    category = models.CharField(max_length=32, null=True, verbose_name='分类')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    editor = models.CharField(max_length=32, default='MD', verbose_name='编辑器')
    access_count = models.BigIntegerField(default=0, verbose_name='阅读量')
