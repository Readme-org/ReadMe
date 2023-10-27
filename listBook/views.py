from django.shortcuts import render
from main.models import Book
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_list(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, "list.html", context)