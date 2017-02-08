# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0010_evidence'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='badgeapp.Achievement', null='True'),
        ),
    ]
