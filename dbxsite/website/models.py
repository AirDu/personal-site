from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from tutorial.models import Tutorial


class Article(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='标题')
    content = models.TextField(null=True, verbose_name='内容')
    # tags = models.CharField(max_length=100, null=True, verbose_name='标签')
    tags = models.ManyToManyField('Tag', null=True, verbose_name='标签', related_name='articles')
    # category = models.CharField(max_length=32, null=True, verbose_name='分类')
    categories = models.ForeignKey('Category', null=True, verbose_name='分类', related_name='articles')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    editor = models.ForeignKey('Editor', null=True, verbose_name='编辑器', related_name='articles')
    access_count = models.BigIntegerField(default=0, verbose_name='阅读量')
    # comments = models.ManyToManyField('Comment', null=True)
    # 1: 发表，0：草稿，-1：删除
    status = models.IntegerField(default=1, verbose_name='状态')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='名称')
    status = models.IntegerField(default=1, verbose_name='状态')

    # articles = models.ManyToManyField('Article', null=True, verbose_name='文章', related_name='+')

    def __str__(self):
        return self.name

    def count(self):
        return len(self.categories.all())


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='名称')
    status = models.IntegerField(default=1, verbose_name='状态')

    # articles = models.ManyToManyField('Article', null=True, verbose_name='文章', related_name='+')

    def __str__(self):
        return self.name

    def count(self):
        return len(self.tags.all())


class Editor(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='编辑器')
    status = models.IntegerField(default=1, verbose_name='状态')


class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField(verbose_name='评论内容')
    # comments = models.ManyToManyField('self', null=True, verbose_name='评论')
    to_comment_from_this = models.ForeignKey('self', null=True, verbose_name='回复评论', related_name='comments')
    to_article_from_this = models.ForeignKey('Article', null=True, verbose_name='回复的文章', related_name='comments')
    to_tutorial_from_this = models.ForeignKey(Tutorial, null=True, verbose_name='回复的教程',
                                              related_name='comments')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    status = models.IntegerField(default=1, verbose_name='状态')
