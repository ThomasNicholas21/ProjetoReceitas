from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenVerifySerializer
)

from django.contrib.auth.models import update_last_login
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        ]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        super().validate(attrs)

        refresh = self.get_token(self.user)
        user_data = UserSerializer(self.user).data

        update_last_login(None, self.user)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": user_data,
        }


class CustomVerifySerializer(TokenVerifySerializer):
    def validate(self, attrs):
        super().validate(attrs)
        return {
            "access-token": "Is Valid"
        }
