from rest_framework import serializers
from .models import Profile, AdditionalProfile
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = settings.AUTH_USER_MODEL,
        fields = ('username', 'email', 'password')


class AdditionalProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdditionalProfile
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    additional_profiles = AdditionalProfileSerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'
