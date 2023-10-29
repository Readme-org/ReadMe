from django.shortcuts import render
from main.models import Book
from listBook.models import myBook
from ratingBook.models import Rating

# Create your views here.
def show_details(request, id):
    book = Book.objects.get(pk = id)
    reviews = Rating.objects.filter(book_id=id)
    is_reviewed = Rating.objects.filter(book_id=id, user=request.user).exists()
    user_review = None
    if is_reviewed:
        user_review = Rating.objects.get(book_id=id, user=request.user)

    context = {
        'name': request.user.username,
        'book': book,
        'reviews': reviews,
        'is_reviewed': is_reviewed,
        'user_review': user_review,
    }

    return render(request, "details.html", context)

def show_details_myBook(request, id):
    book = myBook.objects.get(pk = id)

    context = {
        'name': request.user.username,
        'book': book,
    }

    return render(request, "details_myBook.html", context)