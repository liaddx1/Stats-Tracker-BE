from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from .serializers import TokenUserSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TokenUserSerializer
    permission_classes = [IsAdminUser]


class CurrentUserView(APIView):
    def get(self, request):
        profile = request.user.userprofile
        data = request.user.userdata
        context = {
            "username": request.user.username,
            "is_staff": request.user.is_staff,
            "user_profile": profile,
            "user_data": data,
        }
        serializer = UserSerializer(context)
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
