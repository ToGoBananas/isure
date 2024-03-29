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

    activate_addr = models.CharField('Адрес активации', max_length=300, blank=True, null=True)
    activate_coords = models.CharField('Координаты активации', max_length=100, blank=True, null=True)

    owner = models.ForeignKey(Profile, verbose_name='Владелец', blank=True)

    activation_date = models.DateField('Дата начала действия полиса')
    end_date = models.DateField('Дата окончания действия полиса')

    insure_type = models.CharField('тип страхования', max_length=70)
    PAYMENT_STATUS = Choices('отменен', 'проверка', 'завершен')
    payment_status = models.CharField(max_length=255, blank=True, null=True, choices=PAYMENT_STATUS)
    DELIVERY_STATUS = Choices('запрошен', 'создан', 'загружен на клиент')
    delivery_status = models.CharField('статус доставки', choices=DELIVERY_STATUS, max_length=25)
    pdf = models.URLField(null=True, blank=True)
    jpg = models.URLField(null=True, blank=True)

    exchange_rate = models.FloatField(null=True, blank=True)
    cost_val = models.FloatField(null=True, blank=True)
    cost_rub = models.FloatField()

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
    owner_insured = models.BooleanField(default=True)
    insured_list = models.ManyToManyField(AdditionalProfile, blank=True)

    class Meta:
        verbose_name = 'взр'
        verbose_name_plural = 'ВЗР'


class IFLPolicy(models.Model):
    policy = models.ForeignKey(PolicyBase, null=True)
    property = models.OneToOneField('InsuredProperty', null=True, blank=True)

    def __str__(self):
        return self.policy.insure_type

    class Meta:
        verbose_name = 'ифл'
        verbose_name_plural = 'ИФЛ'


class NSPolicy(models.Model):
    policy = models.ForeignKey(PolicyBase)
    owner_insured = models.BooleanField(default=True)
    insured_list = models.ManyToManyField(AdditionalProfile, blank=True)

    class Meta:
        verbose_name = 'нc'
        verbose_name_plural = 'НC'

    def __str__(self):
        return self.policy.insure_type


class InsuredProperty(models.Model):
    name = models.CharField('Название собсвенности', max_length=100)
    country = models.CharField('страна', max_length=20)
    region = models.CharField('регион', max_length=100, null=True, blank=True)
    city = models.CharField('город', max_length=100)
    street = models.CharField('улица', max_length=100)
    bld_letter = models.CharField('строение\литера', max_length=10,
                                  blank=True, default='', null=True)
    bld_child = models.CharField('корпус', max_length=10,
                                 blank=True, default='', null=True)
    apartment = models.CharField('квартира', max_length=10, null=True, blank=True)

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