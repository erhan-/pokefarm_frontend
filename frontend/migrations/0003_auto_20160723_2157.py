# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_connection_port'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='connect',
            new_name='connection',
        ),
    ]
