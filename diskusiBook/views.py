from django.shortcuts import render
from main.views import Book

# Create your views here.
def show_diskusi(request, id):
    book = Book.objects.get(pk = id)

    context = {
        'book': book,
    }

    return render(request, "diskusi.html", context)