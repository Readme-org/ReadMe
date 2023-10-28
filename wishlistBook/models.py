from django.db import models
from main.models import Book

# Create your models here.

class WishlistBook(models.Model):
    title = models.CharField(max_length=255)
    display_title = models.CharField(max_length=255)
    authors = models.TextField()
    image = models.TextField()