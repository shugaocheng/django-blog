# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170311_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL, related_name='blog_posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='帖子内容'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(verbose_name='发布时间', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(verbose_name='标签', unique_for_date='publish', max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(default='draft', verbose_name='状态', choices=[('draft', 'Draft'), ('published', 'Published')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(verbose_name='修改时间', auto_now=True),
        ),
    ]
