from .models import Profile, AdditionalProfile
from .serializers import ProfileSerializer, AdditionalProfileSerializer
from rest_framework import generics


class ProfilesView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class AdditionalProfilesView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = AdditionalProfileSerializer

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return AdditionalProfile.objects.filter(profile=profile)
