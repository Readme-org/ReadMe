from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect, render
from main.models import Book
from listBook.models import myBook
from django.views.decorators.csrf import csrf_exempt
from main.views import max_title
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def show_list(request):
    books = Book.objects.all()

    context = {
        'name': request.user.username,
        'books': books,
    }
    return render(request, "list.html", context)

@login_required(login_url='/login')
def show_list_filter(request, genre):
    temp_books = Book.objects.all()
    books = []

    for i in temp_books:
        if genre in i.genre:
           books.append(i)

    context = {
        'name': request.user.username,
        'books': books,
    }
    return render(request, "list.html", context)

@login_required(login_url='/login')
def show_list_title(request):
    title_query = request.GET.get('title', '')
    temp_books = Book.objects.filter(title__icontains=title_query) 

    context = {
        'name': request.user.username,
        'books': temp_books,
    }
    return render(request, "list.html", context)

@login_required(login_url='/login')
def show_myBook(request):
    books = myBook.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'books': books,
    }
    return render(request, "myBook.html", context)

def get_book(request):
    books = myBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', books))

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        display_title = max_title(title)
        authors = request.POST.get("authors")
        image = request.POST.get("image")
        description = request.POST.get("description")
        isbn = request.POST.get("isbn")
        user = request.user

        new_book = myBook(
            title=title, 
            display_title=display_title, 
            authors=authors, 
            image=image, 
            description=description,
            isbn=isbn,
            user=user,
        )
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_book(request, id):
    book = myBook.objects.get(user = request.user, pk = id)
    book.delete()

    return redirect('listBook:show_myBook')
        