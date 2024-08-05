from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from .serializers import TokenUserSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import UserProfile, UserUpdateHistory
from .serializers import *


from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.db.models import Sum

# Restframework
from rest_framework import status
from rest_framework.decorators import api_view, APIView, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TokenUserSerializer
    permission_classes = [IsAdminUser]


class CurrentUserView(APIView):
    def get(self, request):
        context = {
            "username": request.user.username,
            "is_staff": request.user.is_staff,
        }
        serializer = UserSerializer(context)
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        user_id = self.kwargs["user_id"]
        user = User.objects.get(id=user_id)
        profile = UserProfile.objects.get(user=user)
        return profile


class UserUpdateHistoryAPIView(generics.ListAPIView):
    serializer_class = UserUpdateHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserUpdateHistory.objects.filter(user=self.request.user.id)


class UserQuestionnaireView(generics.UpdateAPIView):
    serializer_class = UserDataSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return UserData.objects.get(user=user)

    def perform_update(self, serializer):
        print(f"User {self.request.user.username} has filled the questionnaire")
        serializer.save(user=self.request.user)
