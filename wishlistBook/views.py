from django.shortcuts import render
from main.models import Book
from django.core import serializers

# Create your views here.

def show_wishlist(request):
    books = Book.objects.filter(user=request.user)
    context = {
        'books': books 
    }
    return render(request, "wishlist.html", context)

def get_books_json(request):
    books_wishlist = Book.objects.filter(user=request.user)
    wishlist = []
    for book in books_wishlist:
        wishlist.append({
            'title': book.book.title,
            
        })