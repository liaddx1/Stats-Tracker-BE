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
        token["full_name"] = user.userdata.full_name
        token["has_filled_questionnaire"] = user.userprofile.has_filled_questionnaire
        return token


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source="user_data.email")
    full_name = serializers.ReadOnlyField(source="user_data.full_name")

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "is_staff",
            "user_profile",
        ]


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = "__all__"
        extra_kwargs = {"user": {"required": False}}


class UserUpdateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUpdateHistory
        fields = "__all__"
