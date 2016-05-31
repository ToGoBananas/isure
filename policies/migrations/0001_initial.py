# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IFLPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'ифл',
                'verbose_name_plural': 'ИФЛ',
            },
        ),
        migrations.CreateModel(
            name='InsuredAccident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('на рассмотрении', 'на рассмотрении'), ('отказано', 'отказано')], max_length=20, verbose_name='Cтатус рассмотрения случая')),
                ('user_comment', models.TextField(blank=True, max_length=600, null=True)),
                ('admin_comment', models.TextField(blank=True, max_length=600, null=True)),
            ],
            options={
                'verbose_name': 'страховой случай',
                'verbose_name_plural': 'Страховые случаи',
            },
        ),
        migrations.CreateModel(
            name='InsuredProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название собсвенности')),
                ('country', models.CharField(max_length=20, verbose_name='страна')),
                ('region', models.CharField(max_length=100, verbose_name='регион')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('street', models.CharField(max_length=100, verbose_name='улица')),
                ('bld_letter', models.CharField(blank=True, default='', max_length=10, verbose_name='строение\\литера')),
                ('bld_child', models.CharField(blank=True, default='', max_length=10, verbose_name='корпус')),
                ('apartment', models.CharField(max_length=10, verbose_name='квартира')),
            ],
            options={
                'verbose_name': 'застрахованная собственность',
                'verbose_name_plural': 'Застрахованная собственность',
            },
        ),
        migrations.CreateModel(
            name='NSPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'нc',
                'verbose_name_plural': 'НC',
            },
        ),
        migrations.CreateModel(
            name='PolicyBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('expired', 'expired'), ('active', 'active'), ('upcoming', 'upcoming'), ('canceled', 'canceled')], max_length=15, verbose_name='Cтатус полиса')),
                ('create_addr', models.CharField(blank=True, max_length=300, null=True, verbose_name='Адрес создания')),
                ('create_coords', models.CharField(blank=True, max_length=100, null=True, verbose_name='Координаты места создания')),
                ('activate_addr', models.CharField(blank=True, max_length=300, null=True, verbose_name='Адрес активации')),
                ('activate_coords', models.CharField(blank=True, max_length=100, null=True, verbose_name='Координаты активации')),
                ('activation_date', models.DateField(verbose_name='Дата начала действия полиса')),
                ('end_date', models.DateField(verbose_name='Дата окончания действия полиса')),
                ('insure_type', models.CharField(max_length=70, verbose_name='тип страхования')),
                ('payment_status', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_status', models.CharField(choices=[('запрошен', 'запрошен'), ('создан', 'создан'), ('загружен на клиент', 'загружен на клиент')], max_length=25, verbose_name='статус доставки')),
                ('pdf', models.URLField()),
                ('jpg', models.URLField()),
                ('exchange_rate', models.FloatField(null=True)),
                ('cost_val', models.FloatField()),
                ('cost_rub', models.FloatField()),
                ('cost_total', models.FloatField()),
            ],
            options={
                'verbose_name': 'полис',
                'verbose_name_plural': 'Полисы',
            },
        ),
        migrations.CreateModel(
            name='PolicyInsured',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RequestChanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('Открыто', 'Открыто'), ('В работе', 'В работе'), ('Закрыто', 'Закрыто')], default='Открыто', max_length=20, verbose_name='Cтатус запроса')),
                ('text', models.TextField(max_length=600, null=True)),
                ('police', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policies.PolicyBase')),
            ],
            options={
                'verbose_name': 'запрос изменений',
                'verbose_name_plural': 'Запрос изменений',
            },
        ),
        migrations.CreateModel(
            name='VZRPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory', models.CharField(default='Весь Мир', max_length=20, verbose_name='территория действия')),
                ('sport', models.BooleanField(default=False)),
                ('insured', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='policies.PolicyInsured')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policies.PolicyBase')),
            ],
            options={
                'verbose_name': 'взр',
                'verbose_name_plural': 'ВЗР',
            },
        ),
    ]
