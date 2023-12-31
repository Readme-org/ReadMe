from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    display_title = models.CharField(max_length=255)
    authors = models.TextField()
    image = models.TextField()
    description = models.TextField()
    isbn = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class MyMainBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    display_title = models.CharField(max_length=255)
    authors = models.TextField()
    image = models.TextField()
    description = models.TextField()
    isbn = models.CharField(max_length=255)