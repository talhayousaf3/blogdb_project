from django.urls import path

from .views import (
    PostAPIView,
    AddFollower,
    PostDetailApiView,
    UserSignUpView,
)

urlpatterns = [
    path('posts/', PostAPIView.as_view()),
    path('post/<int:pk>/', PostDetailApiView.as_view()),
    path('follow/<int:pk>/', AddFollower.as_view()),
    path('signup/', UserSignUpView.as_view()),



]
