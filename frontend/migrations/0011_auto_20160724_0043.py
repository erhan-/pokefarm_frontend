# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_auto_20160723_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='loc_latitude',
            field=models.FloatField(default=0.0),
        ),
    ]
