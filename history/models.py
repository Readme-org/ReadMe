from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    is_important = models.BooleanField(default=False)
    tag = models.CharField(max_length=50, blank=True)