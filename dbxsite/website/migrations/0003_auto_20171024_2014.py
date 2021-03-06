# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_article_publish_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='access_count',
            field=models.BigIntegerField(default=0, verbose_name='阅读量'),
        ),
        migrations.AddField(
            model_name='article',
            name='editor',
            field=models.CharField(default='MD', max_length=32, verbose_name='编辑器'),
        ),
        migrations.AddField(
            model_name='article',
            name='modify_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=32, null=True, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(max_length=100, null=True, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='标题'),
        ),
    ]
