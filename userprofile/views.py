from rest_framework import generics, status
from rest_framework.response import Response

from userprofile.models import UserData
from .serializers import RegisterSerializer, UserDataSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username':user.username,
            'email': user.email
        })


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = get_user_model().objects.all()

class UserDataCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserDataSerializer
    def get_queryset(self):
        try:
            return [UserData.objects.get(user = self.request.user)]
        except:
            return None
    
    def get(self, request, *args, **kwargs):
        if not self.get_queryset():
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
        return super().get(request, *args, **kwargs)

class UserDataUpdateListAPIView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserDataSerializer
    queryset = UserData.objects.all()
