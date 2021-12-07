from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from blog.models import Post
from users.managers import CustomUserManager
from users.models import CustomUser
from .serializers import PostSerializer, UserSerializer


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()

    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# class AddFollower(generics.RetrieveUpdateDestroyAPIView):
#
#     def get(self, request, pk):
#         author = Post.objects.get(pk=pk).author
#         followers = self.request.user
#
#         if author in followers.following.all():
#             followers.following.remove(author)
#             author.follower.remove(followers)
#
#         else:
#             followers.following.add(author)
#             author.follower.add(followers)
#         return JsonResponse(
#             {
#                 'status': status.HTTP_200_OK,
#                 'data': "",
#                 'message': "follow" + str(followers.email)
#             }
#         )


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
