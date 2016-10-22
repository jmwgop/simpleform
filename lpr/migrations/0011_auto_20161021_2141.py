# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpr', '0010_auto_20161021_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lpr',
            name='interest_type',
        ),
        migrations.AddField(
            model_name='lpr',
            name='md',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lpr',
            name='ogml',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='cont_dev_days',
            field=models.IntegerField(blank=True),
        ),
    ]
