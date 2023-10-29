from django.db import models
from main.models import Book
from django.contrib.auth.models import User

# Create your models here.

class WishlistBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)