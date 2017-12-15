# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='作品名')),
                ('detail', models.CharField(max_length=300, verbose_name='詳細')),
                ('chapter', models.CharField(max_length=10, verbose_name='章')),
                ('date', models.DateField(verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15, verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capter', models.CharField(max_length=15, verbose_name='章')),
            ],
        ),
        migrations.AddField(
            model_name='art',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Category'),
        ),
    ]
