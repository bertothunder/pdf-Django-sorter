# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-14 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfuploader', '0002_auto_20170314_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='creator',
            field=models.TextField(blank=True, default='', max_length=30, verbose_name='Otro software usado'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='producer',
            field=models.TextField(blank=True, default='', max_length=40, verbose_name='Software usado'),
        ),
    ]
