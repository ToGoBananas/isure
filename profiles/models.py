from model_utils.choices import Choices
from phonenumber_field.modelfields import PhoneNumberField
from model_utils.models import TimeStampedModel
from rest_framework.authtoken.models import Token
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.contenttypes.models import ContentType
from .managers import CustomUserManager
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, User, AbstractUser
from django.conf import settings


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), blank=True, unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return ''

    def get_short_name(self):
        return ''

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    @property
    def profile(self):
        return Profile.objects.get(user=self)

    def __str__(self):
        return str(self.email)


class ProfileBase(TimeStampedModel):
    create_coords = models.CharField('Координаты места создания', max_length=100)
    create_addr = models.CharField(max_length=300, blank=True, null=True)
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

    def __str__(self):
        return str(self.email)


class Profile(ProfileBase):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    use_password = models.BooleanField('Использовать пароль на клиент?', default=False)
    phone = PhoneNumberField('Телефон', max_length=30)
    signature = models.ImageField('Подпись (файл)', upload_to='upload/', blank=True, null=True)

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

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.email

    @property
    def additional_profiles(self):
        return self.additionalprofile_set.all()

    @property
    def token(self):
        return Token.objects.get_or_create(user=self.user)[0].key


class AdditionalProfile(ProfileBase):
    profile = models.ForeignKey(Profile)
    name = models.CharField('название профиля', max_length=150)

    class Meta:
        verbose_name = 'дополнительный профиль'
        verbose_name_plural = 'Дополнительные профили'

    def __str__(self):
        return self.name
