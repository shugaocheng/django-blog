# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_reply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ('created',)},
        ),
    ]
