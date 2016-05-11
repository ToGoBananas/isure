# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20160505_0202'),
        ('policies', '0003_auto_20160511_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestChanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('police', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policies.PolicyBase')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
