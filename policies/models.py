# encoding: utf-8
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from profiles.models import Profile, AdditionalProfile, ProfileBase
from model_utils.choices import Choices
from model_utils.models import TimeStampedModel


class Policy(TimeStampedModel):
    STATUS = Choices('expired', 'active', 'upcoming', 'canceled')
    status = models.CharField('Cтатус полиса', choices=STATUS, max_length=15)
    create_coords = models.CharField('Координаты места создания', max_length=100)

    owner = models.ForeignKey(Profile, verbose_name='Владелец')

    activation_date = models.DateField('Дата активации полиса')
    end_date = models.DateField('Дата окончания действия полиса')
    sum = models.FloatField()

    INSURE_TYPE = Choices('ВЗР', 'ИФЛ')
    insure_type = models.CharField('тип страхования', choices=INSURE_TYPE, max_length=3)

    payment_status = models.CharField(max_length=255, blank=True, null=True)
    DELIVERY_STATUS = Choices('запрошен', 'создан', 'загружен на клиент')
    delivery_status = models.CharField('статус доставки', choices=DELIVERY_STATUS, max_length=25)
    pdf = models.URLField()
    jpg = models.URLField()

    @property
    def created_date(self):
        return self.created.date

    class Meta:
        verbose_name = 'полис'
        verbose_name_plural = 'Полисы'


class InsuredAccident(TimeStampedModel):
    policy = models.ForeignKey(Policy)
    create_coords = models.CharField('Координаты места создания', max_length=100)
    STATUS = Choices('на рассмотрении', 'отказано')
    status = models.CharField('Cтатус рассмотрения случая', choices=STATUS, max_length=20)
    user_comment = models.TextField(max_length=600, blank=True, null=True)
    admin_comment = models.TextField(max_length=600, blank=True, null=True)

    class Meta:
        verbose_name = 'страховой случай'
        verbose_name_plural = 'Страховые случаи'


# class VZRInsuredProfile(models.Model):
#     policy = models.ForeignKey(VZRInsurancePolicy)
#     profile = models.ForeignKey(PolicyBase)
#
#
#
# class InsuredProperty(TimeStampedModel):
#     name = models.CharField('Название собсвенности', max_length=100)
#     country = models.CharField('страна', max_length=20)
#     region = models.CharField('регион', max_length=100)
#     city = models.CharField('город', max_length=100)
#     street = models.CharField('улица', max_length=100)
#     bld_letter = models.CharField('строение\литера', max_length=10,
#                                   blank=True, default='')
#     bld_child = models.CharField('корпус', max_length=10,
#                                  blank=True, default='')
#     apartment = models.CharField('квартира', max_length=10)
#
#     def __str__(self):
#         return self.name