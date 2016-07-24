# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('gauth', models.BooleanField(default=False)),
                ('ptc', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=40)),
                ('token', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Eggs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('km', models.IntegerField()),
                ('km2go', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PokeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poke_id', models.IntegerField()),
                ('base_stamina', models.IntegerField()),
                ('base_attack', models.IntegerField()),
                ('base_defense', models.IntegerField()),
                ('type1', models.IntegerField()),
                ('type2', models.IntegerField()),
                ('base_capture_rate', models.FloatField()),
                ('base_flee_rate', models.FloatField()),
                ('evolution', models.IntegerField()),
                ('candy', models.IntegerField()),
                ('picture', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poke_id', models.IntegerField()),
                ('poke_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.PokeData')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=40)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Account')),
                ('connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Connection')),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField()),
                ('level', models.IntegerField()),
                ('km_walked', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='statistics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Statistics'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Profile'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='poke_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.Pokemon'),
        ),
    ]