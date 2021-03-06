# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='标题')),
                ('content', models.TextField(null=True, verbose_name='内容')),
                ('level', models.IntegerField(verbose_name='等级')),
                ('status', models.IntegerField(default=1, verbose_name='状态')),
                ('next', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tutorial.Tutorial', verbose_name='下一节')),
                ('prev', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tutorial.Tutorial', verbose_name='上一节')),
            ],
        ),
    ]
