# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0039_auto_20160517_0951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membership',
            options={'verbose_name_plural': 'Memberships'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-timestamp'], 'verbose_name': 'braintree_payment', 'verbose_name_plural': 'braintree_payments'},
        ),
        migrations.AlterModelOptions(
            name='usermerchantid',
            options={'verbose_name': 'UserMerchantId', 'verbose_name_plural': 'UserMerchantIds'},
        ),
    ]