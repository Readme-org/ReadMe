from django.db import models
from main.models import Book
from django.contrib.auth.models import User

# Create your models here.
class myBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    display_title = models.CharField(max_length=255)
    authors = models.TextField()
    image = models.TextField()
    description = models.TextField()
    isbn = models.CharField(max_length=255)