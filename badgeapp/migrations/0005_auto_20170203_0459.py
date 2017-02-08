# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badgeapp', '0004_auto_20170201_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, blank=True)),
                ('number', models.IntegerField(max_length=30, blank=True)),
                ('photo', models.ImageField(upload_to='skills', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, blank=True)),
                ('photo', models.ImageField(upload_to='skills', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='photo',
            field=models.ImageField(upload_to='schools', blank=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='photo',
            field=models.ImageField(upload_to='topics', blank=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='badgeapp.Topic'),
        ),
        migrations.AddField(
            model_name='badge',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='badgeapp.Skill'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='badge',
            field=models.ForeignKey(to='badgeapp.Badge', on_delete=django.db.models.deletion.SET_NULL, null='True'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='student',
            field=models.ForeignKey(to='badgeapp.Skill', on_delete=django.db.models.deletion.SET_NULL, null='True'),
        ),
    ]
