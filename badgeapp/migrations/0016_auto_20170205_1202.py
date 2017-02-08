# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0015_auto_20170205_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='evd',
        ),
        migrations.RemoveField(
            model_name='evidence',
            name='achvmnt',
        ),
        migrations.AddField(
            model_name='evidence',
            name='achievement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, to='badgeapp.Achievement', null='True'),
        ),
    ]
