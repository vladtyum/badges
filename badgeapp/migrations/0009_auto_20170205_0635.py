# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0008_auto_20170205_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null='True', to='badgeapp.Student'),
        ),
    ]
