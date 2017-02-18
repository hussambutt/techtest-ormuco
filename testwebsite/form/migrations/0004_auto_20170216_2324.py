# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-16 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20170216_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='cats_or_dogs',
            field=models.CharField(max_length=250, verbose_name='Cats or Dogs?'),
        ),
        migrations.AlterField(
            model_name='list',
            name='favorite_color',
            field=models.CharField(max_length=250, verbose_name='Favorite Color'),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=250, unique=True, verbose_name='Name'),
        ),
    ]
