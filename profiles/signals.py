from .models import Profile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.core.exceptions import ObjectDoesNotExist


@receiver(pre_save, sender=Profile)
def create_auth_token(sender, instance=None, **kwargs):
    try:
        Token.objects.create(user=instance.user)
    except ObjectDoesNotExist:
        pass
