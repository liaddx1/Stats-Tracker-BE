from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserData, UserProfile, UserUpdateHistory, Notification


class TokenUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_id"] = user.id
        token["username"] = user.username
        token["is_staff"] = user.is_staff
        token["has_filled_questionnaire"] = user.userprofile.has_filled_questionnaire
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "is_staff",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source="user_data.email")

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = "__all__"
        extra_kwargs = {"user": {"required": False}}


class UserUpdateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUpdateHistory
        fields = "__all__"
