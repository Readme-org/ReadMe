from django.shortcuts import render
from main.models import Book

# Create your views here.
def show_details(request, id):
    book = Book.objects.get(pk = id)

    context = {
        'name': request.user.username,
        'book': book,
    }

    return render(request, "details.html", context)