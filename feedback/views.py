from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework import generics


class FeedbackView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()