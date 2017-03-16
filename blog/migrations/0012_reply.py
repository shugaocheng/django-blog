# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170314_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('to_user', models.CharField(max_length=80)),
                ('body', models.TextField(verbose_name='内容')),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('active', models.BooleanField(default=True, verbose_name='状态')),
                ('comment', models.ForeignKey(to='blog.Comment', verbose_name='评论', related_name='replys')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
