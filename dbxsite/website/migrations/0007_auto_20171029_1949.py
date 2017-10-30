# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 11:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorial', '0001_initial'),
        ('website', '0006_auto_20171029_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('status', models.IntegerField(default=1, verbose_name='状态')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.IntegerField(default=1, verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.IntegerField(default=1, verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='editor',
            name='status',
            field=models.IntegerField(default=1, verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='tag',
            name='status',
            field=models.IntegerField(default=1, verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='comment',
            name='to_article_from_this',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='website.Article', verbose_name='回复的文章'),
        ),
        migrations.AddField(
            model_name='comment',
            name='to_comment_from_this',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='website.Comment', verbose_name='回复评论'),
        ),
        migrations.AddField(
            model_name='comment',
            name='to_tutorial_from_this',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tutorial.Tutorial', verbose_name='回复的教程'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]