# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0002_auto_20160505_0216'),
        ('configuration', '0002_apprules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bordereau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(upload_to='bordereau/')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('insure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policies.Policy')),
            ],
            options={
                'verbose_name': 'бордеро',
                'verbose_name_plural': 'Бордеро',
            },
        ),
    ]
