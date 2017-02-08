# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0012_evidence_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evidence',
            old_name='achievement',
            new_name='achvmnt',
        ),
        migrations.AddField(
            model_name='achievement',
            name='evd',
            field=models.ForeignKey(to='badgeapp.Evidence', on_delete=django.db.models.deletion.SET_NULL, null='True'),
        ),
    ]
