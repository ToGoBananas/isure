from rest_framework import serializers
from .models import Profile, AdditionalProfile, CustomUser
from django.conf import settings


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('user', 'id')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = CustomUser.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


class AdditionalProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdditionalProfile
        fields = '__all__'
