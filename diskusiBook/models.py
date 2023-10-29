from django.db import models
from django.urls import reverse
from main.models import Book
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.

def get_default_post():
    return Post.objects.get_or_create(content="test")[0]

def get_default_book():
    return Book.objects.get_or_create(title="test")[0]

def get_default_comment():
    return Comment.objects.get_or_create(content="test")[0]
    
class Post(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
