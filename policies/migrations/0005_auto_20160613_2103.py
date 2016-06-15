# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0004_auto_20160613_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policybase',
            name='cost_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='policybase',
            name='cost_val',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='policybase',
            name='exchange_rate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
