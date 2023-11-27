from django.contrib.auth.models import User, Group
from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "desc"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_superuser",
            "is_staff",
        ]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
