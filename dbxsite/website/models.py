from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='标题')
    content = models.TextField(null=True, verbose_name='内容')
    # tags = models.CharField(max_length=100, null=True, verbose_name='标签')
    tags = models.ManyToManyField('Tag', null=True, verbose_name='标签', related_name='tags')
    # category = models.CharField(max_length=32, null=True, verbose_name='分类')
    categories = models.ForeignKey('Category', null=True, verbose_name='分类', related_name='categories')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    editor = models.CharField(max_length=32, default='MD', verbose_name='编辑器')
    access_count = models.BigIntegerField(default=0, verbose_name='阅读量')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='名称')

    # articles = models.ManyToManyField('Article', null=True, verbose_name='文章', related_name='+')

    def __str__(self):
        return self.name

    def count(self):
        return len(self.categories.all())


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='名称')

    # articles = models.ManyToManyField('Article', null=True, verbose_name='文章', related_name='+')

    def __str__(self):
        return self.name

    def count(self):
        return len(self.tags.all())
