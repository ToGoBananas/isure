# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 23:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0003_auto_20160530_0143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nspolicy',
            options={'verbose_name': 'нc', 'verbose_name_plural': 'НC'},
        ),
    ]