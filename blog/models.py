from django.db import models
from django.urls import reverse

from blog2_project.settings import AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey(AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
