from django.db import models
from profiles.models import Profile
from policies.models import PolicyBase

from model_utils.models import TimeStampedModel


class Feedback(TimeStampedModel):
    profile = models.ForeignKey(Profile)
