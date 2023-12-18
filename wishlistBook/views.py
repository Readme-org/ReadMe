from django.shortcuts import redirect, render, get_object_or_404
from listBook.models import myBook
from wishlistBook.models import WishlistBook
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from main.views import Book
from django.core import serializers

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
            "image": book.book.image,
            "description": book.book.description,
      })
    finaljs = json.dumps(temp)
    return HttpResponse(finaljs, content_type='application/json')

def add_wishlist(request, book_id):
    buku = get_object_or_404(Book, id=book_id)
    
    # Periksa apakah buku sudah ada di wishlist pengguna
    existing_wishlist_book = WishlistBook.objects.filter(user=request.user, book=buku)
    
    if existing_wishlist_book.exists():
        return HttpResponse(b"Sudah ada di wishlist", status=200)
    else:
        to_wishlist = WishlistBook(user=request.user, book=buku)
        to_wishlist.save()
        return HttpResponse(b"Ditambah", status=201)

@csrf_exempt
def deleteWishlist(request, book_id):
    buku = WishlistBook.objects.get(pk=id)
    buku.delete()
    return JsonResponse({"status": "Berhasil dihapus"})

@login_required
def get_json(request):
    buku = WishlistBook.objects.filter(user=request.user)
    temp = []
    for book in buku:
        temp.append({
            "title": book.book.title,
            "penulis": book.book.authors,
            "isbn": book.book.isbn,
            "image": book.book.image,
            "description": book.book.description,
      })
    finaljs = json.dumps(temp)
    return HttpResponse(finaljs, content_type='application/json')

@csrf_exempt
@login_required
def add_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book_id = data.get('book_id')

        # Temukan buku yang akan ditambahkan ke Wishlist
        book = Book.objects.get(id=book_id)

        # Periksa apakah buku sudah ada di Wishlist
        existing_wishlist_book = WishlistBook.objects.filter(user=request.user, book=book)

        if existing_wishlist_book.exists():
            return JsonResponse({"status": "Buku sudah ada di Wishlist"}, status=200)
        else:
            # Tambahkan buku ke Wishlist pengguna
            new_wishlist_book = WishlistBook.objects.create(user=request.user, book=book)
            return JsonResponse({"status": "Buku berhasil ditambahkan ke Wishlist"}, status=201)
    else:
        return JsonResponse({"status": "Metode tidak diizinkan"}, status=405)