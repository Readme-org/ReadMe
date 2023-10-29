import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from wishlistBook.models import WishlistBook
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def show_wishlist(request):
    books = WishlistBook.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'books': books, 
    }
    return render(request, "wishlist.html", context)

def get_books_json(request):
    books_wishlist = WishlistBook.objects.filter(user=request.user)
    wishlist = []
    for book in books_wishlist:
        wishlist.append({
            'title': book.book.title,
            'display_title': book.book.display_title,
            'authors': book.book.authors,
            'image': book.book.image,
        })
    final = json.dumps(wishlist)
    return HttpResponse(final, content_type ='application/json')

def deleteWishlist(request, id):
    wishlist = WishlistBook.objects.get(pk=id)
    wishlist.delete()
    return HttpResponse(b"Deleted", 201)