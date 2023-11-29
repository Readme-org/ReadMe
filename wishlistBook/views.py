from django.shortcuts import render, get_object_or_404
from listBook.models import myBook
from wishlistBook.models import WishlistBook
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from main.views import Book

@login_required(login_url='/login')
def show_wishlist(request):
    books = WishlistBook.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'books': books,
    }
    return render(request, "wishlist.html", context)

@csrf_exempt
def get_books_json(request):
    buku = WishlistBook.objects.filter(user=request.user)
    temp = []
    for book in buku:
        temp.append({
            "title": book.book.title,
            "penulis": book.book.authors,
            "isbn": book.book.isbn,
            "image": book.book.image
      })
    finaljs = json.dumps(temp)
    return HttpResponse(finaljs, content_type='application/json')

def add_wishlist(request, book_id):
    buku = get_object_or_404(Book, id=book_id)
    to_wishlist = WishlistBook(user = request.user, book = buku)
    to_wishlist.save()
    return HttpResponse(b"Ditambah", status=201)

@csrf_exempt
def deleteWishlist(request, id):
    user = request.user
    try:
        wishlist = WishlistBook.objects.get(user=user, book_id=id)
        wishlist.delete()
        return HttpResponse(b"DELETED", status=201)
    except WishlistBook.DoesNotExist:
        return HttpResponse(b"NOT FOUND", status=404)