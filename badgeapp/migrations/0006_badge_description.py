# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0005_auto_20170203_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
