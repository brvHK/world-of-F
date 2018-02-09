# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-06 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_artimage_is_in_dark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artimage',
            name='art',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='art', to='cms.Art', verbose_name='作品'),
        ),
    ]