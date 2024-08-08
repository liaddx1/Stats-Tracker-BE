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
from .utils import (
    send_welcome_email,
    send_which_user_filled_questionnaire,
    send_contact_us_email_to_us,
    send_contact_us_email_to_client,
)
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

    def update_user_profile(self, user):
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

        try:
            user_data = UserData.objects.get(user=request.user)
        except UserData.DoesNotExist:
            user_data = UserData(user=request.user)

        serializer = self.get_serializer(user_data, data=request.data)

        if serializer.is_valid():
            serializer.save()

            self.update_user_profile(request.user)

            send_welcome_email(email, request.data.get("full_name"))
            send_which_user_filled_questionnaire(request.data.get("full_name"))
            return Response({"message": "User data updated and welcome email sent"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactUsView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        full_name = request.data.get("full_name")
        phone = request.data.get("phone")
        email = request.data.get("email")
        content = request.data.get("content")

        if not email:
            return Response(
                {"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        send_contact_us_email_to_client(full_name, email)
        send_contact_us_email_to_us(full_name, email, phone, content)
        return Response(
            {"message": "Sent!"},
            status=status.HTTP_200_OK,
        )
