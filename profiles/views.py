from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication


class ProfilesView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (TokenAuthentication, )

