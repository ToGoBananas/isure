# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 23:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalprofile',
            options={'verbose_name': 'дополнительный профиль', 'verbose_name_plural': 'Дополнительные профили'},
        ),
    ]
