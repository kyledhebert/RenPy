# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160129_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
