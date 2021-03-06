# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-01-18 08:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20160730_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='cash_intra',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='cash_positional',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='confirmed_phone',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_privileged',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='multi_bagger',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='nifty_future',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='option_calls_covered',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='option_calls_uncovered',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='stock_future',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='subscription_enddate',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='subscription_startdate',
        ),
        migrations.DeleteModel(
            name='order',
        ),
    ]
