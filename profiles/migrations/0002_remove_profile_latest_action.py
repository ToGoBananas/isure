# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='latest_action',
        ),
    ]
