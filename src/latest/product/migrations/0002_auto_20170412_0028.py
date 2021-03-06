# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='c', max_length=128, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='p', max_length=128, unique=True),
            preserve_default=False,
        ),
    ]
