# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-17 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20170216_2324'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Form',
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Name'),
        ),
    ]