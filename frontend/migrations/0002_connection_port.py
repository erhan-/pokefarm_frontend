# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='port',
            field=models.IntegerField(default=5008),
            preserve_default=False,
        ),
    ]
