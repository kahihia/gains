# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 08:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160705_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 7, 6, 8, 2, 51, 474299, tzinfo=utc)),
        ),
    ]
