# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-21 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('block', '0004_block_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.CharField(max_length=100000, verbose_name='内容')),
                ('status', models.IntegerField(choices=[(0, '正常'), (-1, '删除')], verbose_name='状态')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('lastupdate_timestamp', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block', verbose_name='板块ID')),
            ],
            options={
                'verbose_name_plural': '文章(s)',
                'verbose_name': '文章',
            },
        ),
    ]
