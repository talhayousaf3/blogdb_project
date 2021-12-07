from rest_framework import serializers

from blog.models import Post, Comment
from users.managers import CustomUserManager
from users.models import CustomUser


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'author', )


class PostSerializer(serializers.ModelSerializer):
    reviews = CommentSerializer(many=True)

    class Meta:
        model = Post

        fields = ('title', 'author', 'body', 'likes', 'reviews', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        manager_class = CustomUserManager
        fields = ['email', 'password', 'follower', 'following', ]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['email'], validated_data['password'])

        return user
