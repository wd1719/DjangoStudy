# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-21 03:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='manager',
            new_name='manager_name',
        ),
    ]
