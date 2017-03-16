# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('body', models.TextField(verbose_name='回复内容')),
                ('created', models.DateTimeField(verbose_name='回复时间', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('active', models.BooleanField(default=True, verbose_name='状态')),
                ('comment', models.ForeignKey(verbose_name='评论', related_name='replys', to='blog.Comment')),
                ('from_user', models.ForeignKey(verbose_name='回复用户', related_name='reply_user', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(to='blog.Post')),
                ('to_user', models.ForeignKey(verbose_name='被回复用户', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
