from django.db import models
from django.urls import reverse

from blog2_project.settings import AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey(AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               )
    body = models.TextField()
    cover = models.ImageField(upload_to='covers/', blank=True)
    likes = models.ManyToManyField(AUTH_USER_MODEL, related_name='blogpost_like')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
