from django.shortcuts import render
from main.models import Book

# Create your views here.
def show_wishlist(request):
    context = {
        'name': 'Testing',
        'class': 'Test'
    }

    return render(request, "wishlist.html", context)