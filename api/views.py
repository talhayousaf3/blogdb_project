from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from blog.models import Post
from users.managers import CustomUserManager
from users.models import CustomUser
from .serializers import PostSerializer, UserSerializer


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('title', 'author', 'reviews',)
    serializer_class = PostSerializer


class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserSignUpView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    manager_class = CustomUserManager
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
