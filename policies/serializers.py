from rest_framework import serializers
from .models import IFLPolicy, VZRPolicy, NSPolicy, InsuredAccident, RequestChanges, PolicyBase, InsuredProperty
from profiles.serializers import ProfileSerializer, AdditionalProfileSerializer
from profiles.models import AdditionalProfile


class InsuredPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuredProperty
        fields = '__all__'


class PolicyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyBase
        fields = '__all__'


class IFLPolicySerializer(serializers.ModelSerializer):
    policy = PolicyBaseSerializer()
    property = InsuredPropertySerializer()

    def create(self, validated_data):
        policy_data = validated_data.pop('policy')
        policy_base = PolicyBase.objects.create(**policy_data)
        property_data = validated_data.pop('property')
        property = InsuredProperty.objects.create(**property_data)
        return IFLPolicy.objects.create(policy=policy_base, property=property, **validated_data)

    class Meta:
        model = IFLPolicy
        depth = 1
        fields = '__all__'


class VZRPolicySerializer(serializers.ModelSerializer):
    accidents = serializers.ReadOnlyField()
    policy = PolicyBaseSerializer()

    def create(self, validated_data):
        policy_data = validated_data.pop('policy')
        policy_base = PolicyBase.objects.create(**policy_data)
        insured_list = validated_data.pop('insured_list')
        vzr_policy = VZRPolicy.objects.create(policy=policy_base, **validated_data)
        for insured in insured_list:
            vzr_policy.insured_list.add(insured)
        vzr_policy.save()
        return vzr_policy

    class Meta:
        model = VZRPolicy
        fields = '__all__'


class NSPolicySerializer(serializers.ModelSerializer):
    policy = PolicyBaseSerializer()

    class Meta:
        model = NSPolicy
        fields = '__all__'

    def create(self, validated_data):
        policy_data = validated_data.pop('policy')
        policy_base = PolicyBase.objects.create(**policy_data)
        insured_list = validated_data.pop('insured_list')
        ns_policy = NSPolicy.objects.create(policy=policy_base, **validated_data)
        for insured in insured_list:
            ns_policy.insured_list.add(insured)
            ns_policy.save()
        return ns_policy


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
