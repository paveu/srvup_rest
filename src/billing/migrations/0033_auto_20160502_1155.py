# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 11:55
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billing', '0032_auto_20160502_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionPayu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=255)),
                ('extorder_id', models.CharField(blank=True, max_length=120, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('transaction_status', models.CharField(choices=[(b'NEW', b'New'), (b'PENDING', b'Pending'), (b'WAITING_FOR_CONFIRMATION', b'Waiting for confirmation'), (b'COMPLETED', b'Completed'), (b'CANCELED', b'Canceled'), (b'REJECTED', b'Rejected')], default=b'NEW', max_length=255)),
                ('pos_id', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_ip', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-timestamp',),
                'verbose_name': 'payu_payment',
                'verbose_name_plural': 'payu_payments',
            },
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 2, 11, 55, 28, 626570, tzinfo=utc), verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 2, 11, 55, 28, 626500, tzinfo=utc), verbose_name=b'Start Date'),
        ),
    ]
