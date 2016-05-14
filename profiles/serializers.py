from rest_framework import serializers
from .models import Profile, AdditionalProfile


class AdditionalProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdditionalProfile
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    additional_profiles = AdditionalProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        depth = 1
        fields = '__all__'
