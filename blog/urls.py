from django.urls import path

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    check_following,
    check_follower,
    FollowView, CommentCreateView, LikeUnlikeView,
)

urlpatterns = [
    path(
        'post/<int:pk>/delete/',
        BlogDeleteView.as_view(),
        name='post_delete'
    ),
    path(
        'post/<int:pk>/edit/',
        BlogUpdateView.as_view(),
        name='post_edit'
    ),
    path(
        'post/new/',
        BlogCreateView.as_view(),
        name='post_new'
    ),
    path(
        'post/<int:pk>/',
        BlogDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'follow/<int:pk>',
        FollowView.as_view(),
        name='follow'
    ),

    path(
        'check_follower/',
        check_follower,
        name='check_follower'
    ),
    path(
        'check_following/',
        check_following,
        name='check_following'
    ),
    path(
        'comment/<int:pk>/',
        CommentCreateView.as_view(),
        name='post_comment'
    ),
    path(
        'like/<int:pk>/',
        LikeUnlikeView.as_view(),
        name='like'
    ),
    path('', BlogListView.as_view(), name='home'),
]
