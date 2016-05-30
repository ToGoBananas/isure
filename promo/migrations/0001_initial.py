# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 22:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0010_remove_profile_promo_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoProfile',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='profiles.Profile')),
                ('personal_code', models.CharField(blank=True, editable=False, max_length=15, unique=True)),
                ('code_activated', models.BooleanField(default=False)),
                ('free_days', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
    ]
