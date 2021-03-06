# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_category', models.CharField(choices=[('WEAPON', 'Weapon'), ('ARMOR', 'Armor'), ('ACCESORY', 'Accesory')], max_length=30)),
                ('product_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('product_quantity', models.IntegerField()),
                ('product_cost', models.FloatField()),
            ],
        ),
    ]
