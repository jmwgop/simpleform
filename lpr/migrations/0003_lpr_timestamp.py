# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lpr', '0002_auto_20161021_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='lpr',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]