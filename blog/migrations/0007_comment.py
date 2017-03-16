# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170312_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=80)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=254)),
                ('body', models.TextField(verbose_name='评论内容')),
                ('created', models.DateTimeField(verbose_name='发表时间', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('active', models.BooleanField(verbose_name='状态', default=True)),
                ('post', models.ForeignKey(verbose_name='帖子外键', to='blog.Post', related_name='comments')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
