# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-23 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180423_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roughcategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='smallcategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='名称'),
        ),
    ]