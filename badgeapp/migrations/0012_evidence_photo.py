# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0011_evidence_achievement'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='photo',
            field=models.ImageField(upload_to='skills', blank=True),
        ),
    ]
