# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpr', '0009_auto_20161021_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lpr',
            name='consent_assign',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='cont_dev',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='damages',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='depth_limit',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='free_royalty',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='horz_pugh',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='lease_revisions',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='max_pooling_acreage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='min_pooling_acreage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='no_surface',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='ogml_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='orri_wi',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='pooling_limit',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='shut_in',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='specific_surface',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='swd',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='ver_pugh',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lpr',
            name='water_well',
            field=models.BooleanField(default=False),
        ),
    ]
