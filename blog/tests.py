import tempfile

from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser
from .models import Post, Comment


class PostModelTest(TestCase):
    image = tempfile.NamedTemporaryFile(suffix=".jpg").name

    def setUp(self, ):
        author = CustomUser.objects.create(email='test@gmail.com', password='test')
        Post.objects.create(
            title='just a test',
            author=author,
            body='this is test',
            cover=self.image,
        )
        post_for_review = Post.objects.get(title='just a test')
        post_for_review.reviews.create(

            comment='nice',
            author=author,
        )

    def test_text_content(self):
        post = Post.objects.get(title='just a test')
        self.assertEqual(f'{post.title}', 'just a test')
        self.assertEqual(f'{post.author}', 'test@gmail.com')
        self.assertEqual(f'{post.cover}', self.image)
        self.assertEqual(f'{post.body}', 'this is test')
        self.assertEqual(f'{Comment.objects.get(post=post)}', 'nice')


class HomePageViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

#
# class PostLike(TestCase):
#     def setUp(self):
#         first_user = CustomUser.objects.create(email='test1@gmail.com', password='test')
#         likes_Post_1 = Post.objects.create(
#             title='test 2 blog',
#             author=first_user,
#             body='test2 ki body',
#
#         )
#         likes_Post_1.likes.add(first_user)
#         print(first_user.blogpost_like.get, "this is the one to watch")
#
#     def test_likes(self):
#         post1 = Post.objects.get(title='test 2 blog')
#         print(post1.likes, "post liker")
#         self.assertEqual(post1.likes, 2)

