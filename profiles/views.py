from .models import Profile, AdditionalProfile
from .serializers import ProfileSerializer, AdditionalProfileSerializer, ProfileCreateSerializer

from rest_framework import generics
from .permissions import ProfilePermission


class ProfileView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    permission_classes = (ProfilePermission, )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProfileCreateSerializer
        else:
            return ProfileSerializer

    def get_object(self):
        user = self.request.user
        return Profile.objects.get(user=user)


class AdditionalProfilesView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = AdditionalProfileSerializer

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return AdditionalProfile.objects.filter(profile=profile)


class CView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)