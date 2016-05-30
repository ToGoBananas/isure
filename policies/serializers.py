from rest_framework import serializers
from .models import IFLPolicy, VZRPolicy, NSPolicy, InsuredAccident, RequestChanges, PolicyBase
from profiles.serializers import ProfileSerializer


class PolicyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyBase
        fields = '__all__'


class IFLPolicySerializer(serializers.ModelSerializer):
    policy = PolicyBaseSerializer()

    class Meta:
        model = IFLPolicy
        depth = 1
        fields = '__all__'


class VZRPolicySerializer(serializers.ModelSerializer):
    accidents = serializers.ReadOnlyField()
    policy = PolicyBaseSerializer()

    class Meta:
        model = VZRPolicy
        depth = 3
        fields = '__all__'


class NSPolicySerializer(serializers.ModelSerializer):
    policy = PolicyBaseSerializer()
    accidents = serializers.ReadOnlyField()

    class Meta:
        model = NSPolicy
        fields = '__all__'

    def create(self, validated_data):
        policy_data = validated_data.pop('policy')
        policy = PolicyBase.objects.create(**policy_data)
        return NSPolicy.objects.create(policy=policy, **validated_data)


class InsuredAccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuredAccident
        depth = 1
        fields = '__all__'


class RequestChangesSerializer(serializers.ModelSerializer):
    policy = PolicyBaseSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = RequestChanges
        depth = 1
        fields = '__all__'
