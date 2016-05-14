from .models import PolicyBase, IFLPolicy, VZRPolicy, NSPolicy, InsuredAccident, RequestChanges
from profiles.models import Profile
from .serializers import IFLPolicySerializer, VZRPolicySerializer, NSPolicySerializer,\
    InsuredAccidentSerializer, RequestChangesSerializer, PolicyBaseSerializer

from rest_framework import generics


class IFLView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = IFLPolicySerializer

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return IFLPolicy.objects.filter(policy__owner=profile)


class VZRView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = VZRPolicySerializer

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return VZRPolicy.objects.filter(policy__owner=profile)


class NSPView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = NSPolicySerializer

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return NSPolicy.objects.filter(policy__owner=profile)


class InsuredAccidentView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = InsuredAccidentSerializer
    queryset = InsuredAccident.objects.all()


class RequestChangesView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = RequestChangesSerializer

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return RequestChanges.objects.filter(profile=profile)


class PolicyBaseView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = PolicyBaseSerializer
    queryset = PolicyBase.objects.all()
