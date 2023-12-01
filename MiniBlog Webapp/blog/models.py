from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    # this will order comments based on publish date
    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f'Comment by {self.name}'


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    uploaded_at = models.DateTimeField(default=timezone.now)
