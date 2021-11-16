from rest_framework import serializers

from blog.models import Post
from users.managers import CustomUserManager
from users.models import CustomUser


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        manager_class = CustomUserManager
        fields = ['email', 'password', ]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['email'], validated_data['password'])

        return user
