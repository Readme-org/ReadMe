from django.shortcuts import render
from main.models import Book
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_list(request):
    books = Book.objects.all()

    context = {
        'name': request.user.username,
        'books': books,
    }
    return render(request, "list.html", context)

def show_myBook(request):
    books = Book.objects.all()

    context = {
        'name': request.user.username,
        'books': books,
    }
    return render(request, "myBook.html", context)