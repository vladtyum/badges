# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0003_school_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='badgeapp.School'),
        ),
    ]
