# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20180403_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank='true', default='abc', unique=True),
        ),
    ]
