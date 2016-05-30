from django.db import models
from profiles.models import Profile
import random
import string


class PromoProfile(models.Model):
    profile = models.OneToOneField(Profile, primary_key=True)
    personal_code = models.CharField(max_length=15, blank=True, unique=True, editable=False)
    code_activated = models.BooleanField(default=False, blank=True)
    free_days = models.PositiveIntegerField(default=0, blank=True)

    def save(self, *args, **kwargs):
        if not self.personal_code:
            self.personal_code = generate_code(15)
        super(PromoProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.personal_code


def generate_code(length):
    char_set = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(char_set) for _ in range(length))

    while PromoProfile.objects.filter(personal_code=code).exists():
        code = ''.join(random.choice(char_set) for _ in range(length))

    return code
