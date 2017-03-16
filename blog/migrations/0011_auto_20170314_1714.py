# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170314_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='post',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
