# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0014_auto_20170205_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='evd',
            field=models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, null='True', blank=True, to='badgeapp.Evidence'),
        ),
    ]
