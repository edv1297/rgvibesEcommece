# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
