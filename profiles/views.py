from .models import Profile, AdditionalProfile, CustomUser
from .serializers import ProfileSerializer, AdditionalProfileSerializer, UserSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics


class ProfilesView(generics.ListAPIView, generics.UpdateAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny, )


class AdditionalProfilesView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = AdditionalProfileSerializer

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return AdditionalProfile.objects.filter(profile=profile)


class CView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return self.create(request, *args, **kwargs)