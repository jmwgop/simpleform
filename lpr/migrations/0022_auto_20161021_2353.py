# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpr', '0021_auto_20161021_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lpr',
            name='ogml',
            field=models.BooleanField(default=False),
        ),
    ]
