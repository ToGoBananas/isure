from django.contrib import admin
from .models import Profile, AdditionalProfile

admin.site.register(AdditionalProfile)
admin.site.register(Profile)
