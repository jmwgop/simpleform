# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 23:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lpr', '0016_auto_20161021_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lpr',
            old_name='bonus_Per_Acre',
            new_name='bonus_per_Acre',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='check_Number',
            new_name='check_number',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='continuious_Devlopment',
            new_name='cont_dev',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='continuious_Devlopment_Period_in_Days',
            new_name='cont_dev_period_days',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='depth_Limitation',
            new_name='depth_limitation',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='drilling_Platform',
            new_name='drilling_platform',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='effective_Date',
            new_name='effective_date',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='expiration_Date',
            new_name='expiration_date',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='extension_Term_in_Years',
            new_name='extension_term_in_years',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='gross_Acres',
            new_name='gross_acres',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='horziontal_Pugh_Clause',
            new_name='horziontal_pugh',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='Lease_Revisions',
            new_name='lease_revisions',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='lessor_Address_1',
            new_name='lessor_address1',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='lessor_Address_2',
            new_name='lessor_address2',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='lessor_City',
            new_name='lessor_city',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='lessor_Email',
            new_name='lessor_email',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='lessor_Interest',
            new_name='lessor_interest',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='lessor_Phone',
            new_name='lessor_phone',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='lessor_SSN_or_TIN',
            new_name='lessor_ssntin',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='lessor_State',
            new_name='lessor_state',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='lessor_Zip',
            new_name='lessor_zip',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='mineral_Deed',
            new_name='md',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='net_Acres',
            new_name='net_acres',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='oRRI_WI',
            new_name='ogml_only',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='oil_and_Gas_Only',
            new_name='orri_wi',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='primary_Term_in_Years',
            new_name='primary_term_in_years',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='sWD',
            new_name='swd',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='total_Bonus',
            new_name='total_bonus',
        ),
        migrations.RenameField(
            model_name='lpr',
            old_name='ver_Pugh_Clause',
            new_name='vertical_pugh',
        ),
    ]
