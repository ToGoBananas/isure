from .models import Bordereau
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files.base import ContentFile

# from .helpers import get_bordereau
#
#
# @receiver(pre_save, sender=Bordereau)
# def create_file(sender, instance=None, **kwargs):
#     if not instance.csv:
#         instance.csv.save('test.csv', ContentFile(get_bordereau(instance.start, instance.end)))
