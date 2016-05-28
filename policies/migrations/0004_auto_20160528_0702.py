# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0003_insuredaccident_create_addr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insuredaccident',
            name='create_addr',
        ),
        migrations.RemoveField(
            model_name='insuredaccident',
            name='create_coords',
        ),
        migrations.AddField(
            model_name='policybase',
            name='create_addr',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
