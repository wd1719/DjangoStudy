# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-21 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_auto_20161021_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='links',
            field=models.CharField(default='', max_length=100, verbose_name='链接网址'),
        ),
    ]
