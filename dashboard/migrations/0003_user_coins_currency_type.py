# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-25 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170925_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_coins',
            name='currency_type',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]