from rest_framework import serializers
from .models import Profile, AdditionalProfile, CustomUser
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'password',)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        depth = 1
        fields = '__all__'


class ProfileCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        return Profile.objects.create(user=user, **validated_data)


class AdditionalProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdditionalProfile
        fields = '__all__'
