from django.shortcuts import render, get_object_or_404
from listBook.models import myBook
from wishlistBook.models import WishlistBook
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from main.views import Book

@login_required(login_url='/login')
def show_wishlist(request, id):
    books = get_object_or_404(Book, id=id)
    context = {
        'name': request.user.username,
        'books': books,
    }
    return render(request, "wishlist.html", context)

@csrf_exempt
def get_books_json(request, id_book):
    book = get_object_or_404(Book, id=id)
    created = WishlistBook.objects.get_or_create(user=user, book=book)

    if created:
        return HttpResponse(b"CREATED", status=201)
    else:
        return HttpResponse(b"ALREADY EXIST", status=200)

@csrf_exempt
def deleteWishlist(request, id):
    user = request.user
    try:
        wishlist = WishlistBook.objects.get(user=user, book__id=id)
        wishlist.delete()
        return HttpResponse(b"DELETED", status=201)
    except WishlistBook.DoesNotExist:
        return HttpResponse(b"NOT FOUND", status=404)