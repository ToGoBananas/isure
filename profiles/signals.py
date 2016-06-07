from .models import Profile, AdditionalProfile
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from locations.helpers import get_address_by_geocode


@receiver(pre_save, sender=Profile)
def create_auth_token(sender, instance=None, **kwargs):
    instance.create_addr = get_address_by_geocode(instance.create_coords)
    Token.objects.get_or_create(user=instance.user)



@receiver(pre_save, sender=AdditionalProfile)
def addr(sender, instance=None, **kwargs):
    instance.create_addr = get_address_by_geocode(instance.create_coords)


@receiver(post_delete, sender=Profile)
def delete_related_user(sender, instance=None, **kwargs):
    instance.user.delete()
