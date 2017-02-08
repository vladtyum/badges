# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0016_auto_20170205_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
