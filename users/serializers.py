from rest_framework import serializers
from .models import *
# from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group
from djoser.serializers import UserCreateSerializer


# User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email','password', 'name', 'phone', 'location')
        extra_kwargs = {'password': {'write_only': True}}
       