from django.http import HttpResponse
from django.shortcuts import render
from wishlistBook.models import WishlistBook
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

def show_wishlist_json(request):
    data = WishlistBook.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")