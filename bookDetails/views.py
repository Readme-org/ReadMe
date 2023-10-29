from django.shortcuts import render
from main.models import Book
from listBook.models import myBook
from ratingBook.models import Rating

# Create your views here.
def show_details(request, id):
    book = Book.objects.get(pk = id)
    reviews = Rating.objects.filter(book_id=id)

    context = {
        'name': request.user.username,
        'book': book,
        'reviews': reviews,
    }

    return render(request, "details.html", context)

def show_details_myBook(request, id):
    book = myBook.objects.get(pk = id)

    context = {
        'name': request.user.username,
        'book': book,
    }

    return render(request, "details.html", context)