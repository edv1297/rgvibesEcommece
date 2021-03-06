# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0002_cart_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=120)),
                ('address', models.TextField()),
                ('status', models.CharField(default='Order created', max_length=120)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=5.99, max_digits=8)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
            ],
        ),
    ]
