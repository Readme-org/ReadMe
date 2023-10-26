from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    display_title = models.CharField(max_length=255)
    authors = models.TextField()  # Daftar nama penulis, dipisahkan dengan koma
    image = models.TextField()