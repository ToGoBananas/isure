from django.db import models
from profiles.models import Profile
from policies.models import PolicyBase
from model_utils.choices import Choices
from model_utils.models import TimeStampedModel


class Feedback(TimeStampedModel):
    profile = models.ForeignKey(Profile)
    text = models.CharField(max_length=600, null=True)
    STATUS = Choices('Открыто', 'В работе', 'Закрыто')
    status = models.CharField('Cтатус обращения', choices=STATUS, max_length=20, default='Открыто')

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.profile.user.email
