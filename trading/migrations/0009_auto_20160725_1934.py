# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-25 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0008_auto_20160720_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calls',
            options={'verbose_name_plural': 'calls'},
        ),
    ]