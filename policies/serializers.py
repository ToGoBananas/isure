from rest_framework import serializers
from .models import IFLPolicy, VZRPolicy, NSPolicy


class IFLPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = IFLPolicy
        fields = '__all__'


class VZRPolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = VZRPolicy
        depth = 1
        fields = '__all__'


class NSPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = NSPolicy
        fields = '__all__'
