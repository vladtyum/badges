# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0009_auto_20170205_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, blank=True)),
                ('description', models.CharField(max_length=300, blank=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
