# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0006_badge_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='skill',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.SET_NULL, to='badgeapp.Skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='topic',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.SET_NULL, to='badgeapp.Topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='school',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.SET_NULL, to='badgeapp.School'),
        ),
    ]
