from .models import IFLPolicy, VZRPolicy, NSPolicy
from .serializers import IFLPolicySerializer, VZRPolicySerializer, NSPolicySerializer
from rest_framework import generics


class IFLView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = IFLPolicySerializer
    queryset = IFLPolicy.objects.all()


class VZRView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = VZRPolicySerializer
    queryset = VZRPolicy.objects.all()


class NSPView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = NSPolicySerializer
    queryset = NSPolicy.objects.all()
