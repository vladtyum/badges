# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0013_auto_20170205_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='evd',
            field=models.ForeignKey(to='badgeapp.Evidence', blank=True, null='True', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
