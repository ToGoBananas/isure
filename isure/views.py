from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from profiles.models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token


class GetToken(APIView):
    renderer_classes = (JSONRenderer, )
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']
        user = get_object_or_404(CustomUser, email=email)
        if user.profile.use_password and not user.check_password(password):
            content = {'error': 'wrong password'}
        else:
            token, created = Token.objects.get_or_create(user=user)
            content = {'token': token.key}
        return Response(content)
