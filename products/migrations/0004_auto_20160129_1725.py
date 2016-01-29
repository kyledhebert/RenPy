# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160127_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Order'),
        ),
    ]
