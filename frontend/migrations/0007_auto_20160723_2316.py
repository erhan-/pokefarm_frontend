# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20160723_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokedata',
            name='poke_id',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='individual_id',
            field=models.CharField(max_length=64),
        ),
    ]
