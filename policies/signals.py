from .models import InsuredAccident, VZRPolicy, NSPolicy, IFLPolicy
from django.db.models.signals import pre_save
from django.dispatch import receiver
from locations.helpers import get_address_by_geocode


@receiver(pre_save, sender=InsuredAccident)
@receiver(pre_save, sender=VZRPolicy)
@receiver(pre_save, sender=IFLPolicy)
@receiver(pre_save, sender=NSPolicy)
def save_add(sender, instance=None, **kwargs):
    instance.policy.create_addr = get_address_by_geocode(instance.policy.create_coords)
