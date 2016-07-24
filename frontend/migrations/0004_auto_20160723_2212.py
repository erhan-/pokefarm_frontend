# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20160723_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='poke_id',
            new_name='pokemon_id',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='cp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='cp_multiplier',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='height_m',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='individual_attack',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='individual_defense',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='individual_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='individual_stamina',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='move_1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='move_2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stamina',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stamina_max',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='weight_kg',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='loc_latitude',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
