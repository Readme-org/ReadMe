from django.forms import ModelForm
from listBook.models import myBook

class ProductForm(ModelForm):
    class Meta:
        model = myBook
        fields = ["title", "image", "authors"]