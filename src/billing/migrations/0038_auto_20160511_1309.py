# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 13:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0037_auto_20160504_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 11, 13, 9, 22, 10434, tzinfo=utc), verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 11, 13, 9, 22, 10377, tzinfo=utc), verbose_name=b'Start Date'),
        ),
    ]
