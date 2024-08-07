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
from rest_framework import status
from .utils import send_welcome_email, send_which_user_filled_questionnaire
from .serializers import *


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TokenUserSerializer
    permission_classes = [IsAdminUser]


class CurrentUserView(APIView):
    def get(self, request):
        context = {
            "username": request.user.username,
            "is_staff": request.user.is_staff,
            "user_profile": request.user.userprofile,
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

    def update_user(self):
        # Update the user profile
        user = self.request.user
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.has_filled_questionnaire = True
        user_profile.save()

        print(f"User {self.request.user.username} has filled the questionnaire")

    def put(self, request):
        email = request.data.get("email")
        if not email:
            return Response(
                {"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        send_welcome_email(email)
        send_which_user_filled_questionnaire(request.user.username)

        self.update_user()

        return Response({"message": "Welcome email sent"})
