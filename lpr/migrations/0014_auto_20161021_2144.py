# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 21:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lpr', '0013_auto_20161021_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lpr',
            old_name='lessor_ssn_tin',
            new_name='lessor_SSN_or_TIN',
        ),
    ]