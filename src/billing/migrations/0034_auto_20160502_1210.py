# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 12:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0033_auto_20160502_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 2, 12, 10, 46, 385259, tzinfo=utc), verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 2, 12, 10, 46, 385204, tzinfo=utc), verbose_name=b'Start Date'),
        ),
        migrations.AlterField(
            model_name='transactionpayu',
            name='amount',
            field=models.CharField(max_length=8),
        ),
    ]
