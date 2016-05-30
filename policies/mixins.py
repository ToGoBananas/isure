from profiles.models import Profile
from rest_framework.generics import ListAPIView


class ProfileListAPIView(ListAPIView):

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return self.queryset.filter(policy__owner=profile)