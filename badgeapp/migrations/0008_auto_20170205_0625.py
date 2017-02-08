# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0007_auto_20170203_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='number',
            field=models.IntegerField(blank=True),
        ),
    ]
