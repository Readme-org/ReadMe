from django.shortcuts import render
from listBook.models import myBook
from wishlistBook.models import WishlistBook
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core import serializers

@login_required(login_url='/login')
def show_wishlist(request):
    user = request.user
    wishlist = WishlistBook.objects.filter(user=user)
    context = {
        'books': wishlist,
    }
    return render(request, "wishlist.html", context)

@csrf_exempt
def get_books_json(request, id_book):
    user = request.user
    book = myBook.objects.get(pk=id_book)
    _, created = WishlistBook.objects.get_or_create(user=user, book=book)

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