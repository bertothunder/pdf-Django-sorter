# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-14 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfuploader', '0004_auto_20170314_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='creator',
            field=models.TextField(blank=True, default='', max_length=50, verbose_name='Otro software usado'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='producer',
            field=models.TextField(blank=True, default='', max_length=50, verbose_name='Software usado'),
        ),
    ]
