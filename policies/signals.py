from .models import PolicyBase
from django.db.models.signals import pre_save
from django.dispatch import receiver
from locations.helpers import get_address_by_geocode


@receiver(pre_save, sender=PolicyBase)
def save_add(sender, instance=None, **kwargs):
    if not instance.create_addr and instance.create_coords:
        instance.create_addr = get_address_by_geocode(instance.create_coords)
    if not instance.activate_addr and instance.activate_coords:
        instance.activate_addr = get_address_by_geocode(instance.activate_coords)