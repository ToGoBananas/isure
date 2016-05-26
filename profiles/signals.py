from .models import Profile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from locations.helpers import get_address_by_geocode


@receiver(pre_save, sender=Profile)
def create_auth_token(sender, instance=None, **kwargs):
    instance.create_addr = get_address_by_geocode(instance.create_coords)
    Token.objects.get_or_create(user=instance.user)

