from .models import PolicyBase, IFLPolicy, VZRPolicy, NSPolicy, InsuredAccident, RequestChanges
from profiles.models import Profile
from .serializers import IFLPolicySerializer, VZRPolicySerializer, NSPolicySerializer,\
    InsuredAccidentSerializer, RequestChangesSerializer
from .mixins import ProfileListAPIView

from rest_framework import generics


class IFLView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    serializer_class = IFLPolicySerializer

    def create(self, request, *args, **kwargs):
        request.data['policy']['owner'] = request.user.profile.pk
        return super(IFLView, self).create(request, *args, **kwargs)

    def get_object(self):
        id = self.request.data.get('id')
        profile = self.request.user.profile
        return IFLPolicy.objects.get(id=id, profile=profile)

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return IFLPolicy.objects.filter(policy__owner=profile)


class VZRView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    serializer_class = VZRPolicySerializer

    def create(self, request, *args, **kwargs):
        request.data['policy']['owner'] = request.user.profile.pk
        return super(VZRView, self).create(request, *args, **kwargs)

    def get_object(self):
        id = self.request.data.get('id')
        profile = self.request.user.profile
        return VZRPolicy.objects.get(id=id, profile=profile)

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return VZRPolicy.objects.filter(policy__owner=profile)


class NSView(ProfileListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = NSPolicySerializer

    def create(self, request, *args, **kwargs):
        request.data['policy']['owner'] = request.user.profile.pk
        return super(NSView, self).create(request, *args, **kwargs)

    def get_object(self):
        id = self.request.data.get('id')
        profile = self.request.user.profile
        return NSPolicy.objects.get(id=id, profile=profile)

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
