# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 23:27
from __future__ import unicode_literals

import cms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20170606_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayname', models.CharField(max_length=30, verbose_name='画像名')),
                ('artImage', models.ImageField(upload_to=cms.models.ArtImage.get_image_path, verbose_name='作品の画像')),
            ],
        ),
    ]
