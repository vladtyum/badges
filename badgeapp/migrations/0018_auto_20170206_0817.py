# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0017_auto_20170205_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='name',
            field=models.CharField(unique='True', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(unique='True', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(unique='True', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(unique='True', max_length=30, blank=True),
        ),
    ]
