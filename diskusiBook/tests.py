from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Book
from .models import Post, Comment
from .forms import PostForm

class DiskusiBookViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.book = Book.objects.create(title="Test Book")
        self.post = Post.objects.create(title="Test Post", content="Test Content", user=self.user, book=self.book)
        self.comment = Comment.objects.create(text="Test Comment", user=self.user, post=self.post)
        self.client.login(username="testuser", password="testpassword")
