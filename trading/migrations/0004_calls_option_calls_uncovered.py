# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0003_calls'),
    ]

    operations = [
        migrations.AddField(
            model_name='calls',
            name='option_calls_uncovered',
            field=models.BooleanField(default=False),
        ),
    ]
