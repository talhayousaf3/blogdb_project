from django.urls import path

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    check_following,
    check_follower,
    CommentCreateView,
    # detail_to_pdf,
    FollowView,
    LikeUnlikeView,
    # PdfDetail,

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

    # path(
    #     'pdf_my/<int:pk>/',
    #     detail_to_pdf,
    #     name='pdf'
    # ),
    # path(
    #     'pdf/<int:pk>/',
    #     PdfDetail.as_view(template_name='post_detail.html',
    #                       filename='post_pdf.pdf'),
    #     name='pdf_new'
    # ),

    path('', BlogListView.as_view(), name='home'),
]
