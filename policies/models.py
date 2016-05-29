# encoding: utf-8
from django.db import models
from django.contrib.contenttypes.models import ContentType
from profiles.models import Profile, AdditionalProfile, ProfileBase
from model_utils.choices import Choices
from model_utils.models import TimeStampedModel


class PolicyBase(TimeStampedModel):
    STATUS = Choices('expired', 'active', 'upcoming', 'canceled')
    status = models.CharField('Cтатус полиса', choices=STATUS, max_length=15)
    create_addr = models.CharField('Адрес создания', max_length=300, blank=True, null=True)
    create_coords = models.CharField('Координаты места создания', max_length=100, blank=True, null=True)

    owner = models.ForeignKey(Profile, verbose_name='Владелец')

    activation_date = models.DateField('Дата начала действия полиса')
    end_date = models.DateField('Дата окончания действия полиса')

    insure_type = models.CharField('тип страхования', max_length=70)
    payment_status = models.CharField(max_length=255, blank=True, null=True)
    DELIVERY_STATUS = Choices('запрошен', 'создан', 'загружен на клиент')
    delivery_status = models.CharField('статус доставки', choices=DELIVERY_STATUS, max_length=25)
    pdf = models.URLField()
    jpg = models.URLField()

    exchange_rate = models.FloatField(null=True)
    cost_val = models.FloatField()
    cost_rub = models.FloatField()
    cost_total = models.FloatField()

    @property
    def accidents(self):
        return self.insuredaccident_set.all()

    @property
    def created_date(self):
        return self.created.date

    @property
    def days(self):
        return (self.activation_date - self.end_date).days

    class Meta:
        verbose_name = 'полис'
        verbose_name_plural = 'Полисы'

    def __str__(self):
        return self.insure_type


class InsuredAccident(TimeStampedModel):
    policy = models.ForeignKey(PolicyBase)
    create_coords = models.CharField('Координаты места создания', max_length=100, blank=True, null=True)
    STATUS = Choices('на рассмотрении', 'отказано')
    status = models.CharField('Cтатус рассмотрения случая', choices=STATUS, max_length=20)
    user_comment = models.TextField(max_length=600, blank=True, null=True)
    admin_comment = models.TextField(max_length=600, blank=True, null=True)
    profile = models.ForeignKey(Profile, null=True)
    additional_profile = models.ForeignKey(AdditionalProfile, null=True)

    def get_profile(self):
        if self.profile:
            return self.profile
        else:
            return self.additional_profile

    class Meta:
        verbose_name = 'страховой случай'
        verbose_name_plural = 'Страховые случаи'


class VZRPolicy(models.Model):
    policy = models.ForeignKey(PolicyBase)
    territory = models.CharField('территория действия', max_length=20, default='Весь Мир')
    sport = models.BooleanField(default=False)
    insured = models.OneToOneField('PolicyInsured', null=True)

    class Meta:
        verbose_name = 'взр'
        verbose_name_plural = 'ВЗР'


class IFLPolicy(models.Model):
    policy = models.ForeignKey(PolicyBase, null=True)

    class Meta:
        verbose_name = 'ифл'
        verbose_name_plural = 'ИФЛ'


class NSPolicy(models.Model):
    policy = models.ForeignKey(PolicyBase)
    insured = models.OneToOneField('PolicyInsured', null=True)

    class Meta:
        verbose_name = 'нз'
        verbose_name_plural = 'НЗ'


class InsuredProperty(models.Model):
    name = models.CharField('Название собсвенности', max_length=100)
    country = models.CharField('страна', max_length=20)
    region = models.CharField('регион', max_length=100)
    city = models.CharField('город', max_length=100)
    street = models.CharField('улица', max_length=100)
    bld_letter = models.CharField('строение\литера', max_length=10,
                                  blank=True, default='')
    bld_child = models.CharField('корпус', max_length=10,
                                 blank=True, default='')
    apartment = models.CharField('квартира', max_length=10)

    class Meta:
        verbose_name = 'застрахованная собственность'
        verbose_name_plural = 'Застрахованная собственность'

    def __str__(self):
        return self.name


class RequestChanges(TimeStampedModel):
    profile = models.ForeignKey(Profile)
    police = models.ForeignKey(PolicyBase)
    STATUS = Choices('Открыто', 'В работе', 'Закрыто')
    status = models.CharField('Cтатус запроса', choices=STATUS, max_length=20, default='Открыто')
    text = models.TextField(max_length=600, null=True)

    class Meta:
        verbose_name = 'запрос изменений'
        verbose_name_plural = 'Запрос изменений'

    def __str__(self):
        return self.profile.user.email


class PolicyInsured(models.Model):
    profile = models.ForeignKey(Profile, null=True, blank=True)
    additional_profiles = models.ManyToManyField(AdditionalProfile, blank=True)

    def __str__(self):
        return self.profile.user.email