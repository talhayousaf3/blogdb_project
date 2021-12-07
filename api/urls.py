from django.urls import path
from rest_framework.documentation import include_docs_urls

from .views import (
    PostAPIView,
    # AddFollower,
    PostDetailApiView,
    UserSignUpView,
)



urlpatterns = [
    path('posts/', PostAPIView.as_view()),
    path('post/<int:pk>/', PostDetailApiView.as_view()),
    # path('follow/<int:pk>/', AddFollower.as_view()),
    path('docs/', include_docs_urls(title='Blog API')),

    path('signup/', UserSignUpView.as_view()),

]
