from django.db import models
from django.contrib.auth.models import User
from model_utils.choices import Choices
from phonenumber_field.modelfields import PhoneNumberField
from model_utils.models import TimeStampedModel


class ProfileBase(TimeStampedModel):
    create_coords = models.CharField('Координаты места создания', max_length=100)
    birthdate = models.DateField('Дата рождения')

    SEX = Choices('мужской', 'женский')
    sex = models.CharField('Пол', choices=SEX, max_length=10)

    surname_rus = models.CharField('Фамилия на русском', max_length=50)
    name_rus = models.CharField('Имя на русском', max_length=50)
    midname_rus = models.CharField('Отчество', max_length=50, blank=True, null=True)

    passport_int = models.CharField('Номер загранпаспорта', max_length=50)
    surname_eng = models.CharField('Фамилия на английском', max_length=50)
    name_eng = models.CharField('Имя на английском', max_length=50)

    class Meta:
        abstract = True


class Profile(ProfileBase):
    user = models.OneToOneField(User)

    password = models.CharField('Пароль на клиент', max_length=100)
    phone = PhoneNumberField('Телефон', max_length=20)
    signature = models.FileField('Подпись (файл)', upload_to='upload/')

    passport_rf = models.CharField('Номер пасспорта РФ', max_length=50)

    # Address
    country = models.CharField('страна', max_length=20)
    region = models.CharField('регион', max_length=100)
    city = models.CharField('город', max_length=100)
    street = models.CharField('улица', max_length=100)
    bld_number = models.CharField('дом', max_length=10)
    bld_letter = models.CharField('строение\литера', max_length=10,
                                  blank=True, default='')
    bld_child = models.CharField('корпус', max_length=10,
                                 blank=True, default='')
    apartment = models.CharField('квартира', max_length=10)

    promo_code = models.CharField('промо-код', max_length=50, blank=True, null=True)
    latest_action = models.DateTimeField('последние действие', blank=True, null=True)

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.email

    @property
    def token(self):
        return self.user.token


class AdditionalProfile(ProfileBase):
    profile = models.ForeignKey(Profile)
    name = models.CharField('название профиля', max_length=150)

    class Meta:
        verbose_name = 'дополнительный профиль'
        verbose_name_plural = 'Дополнительные профили'

    def __str__(self):
        return self.profile

