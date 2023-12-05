import json
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Book
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
import requests
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import MyMainBook
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:show_main')

@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def show_main(request):
    context = {
        'name': request.user.username,
        'class': 'Test'
    }

    return render(request, "main.html", context)

BASE_URL = 'https://www.googleapis.com/books/v1/volumes'
API_KEY = "AIzaSyByhU8BReRCv4y_APglq06WoUX0GCEPvns" 

def fetch_books(query, max_results=40):
    """
    Ambil buku dari Google Books API berdasarkan query.
    """
    params = {
        'q': query,
        'key': API_KEY,
        'maxResults': max_results
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    results = response.json()
    books = results.get('items', [])
    return books

def max_title(title, max_length=20):  # mengganti parameter max_words dengan max_length
    if len(title) > max_length:
        return title[:max_length-3] + '...'  # mengurangkan 3 karena kita menambahkan '...'
    return title


def database_make(request):
    Book.objects.all().delete()
    query = [
        "romance comedy",
        "action",
        "Fantasy",
        "fiction",
        "manga",
        "science",
    ]
    for i in range(len(query)):
        books_data = fetch_books(query[i], 20)

        # Potong setiap judul buku
        for book_data in books_data:
            title = book_data['volumeInfo']['title']
            authors = ", ".join(book_data['volumeInfo'].get('authors', []))
            image = book_data['volumeInfo']['imageLinks']['thumbnail']
            description = book_data['volumeInfo'].get('description', 'No description available')
            industryIdentifiers = book_data['volumeInfo'].get('industryIdentifiers', [])
            isbn = ""
            genre = query[i]
            
            for identifier in industryIdentifiers:
                if identifier['type'] == 'ISBN_13':
                    isbn = identifier['identifier']
                    break

            book = Book(
                title=title,
                display_title=max_title(title),
                authors=authors,
                image=image,
                description=description,
                isbn=isbn,
                genre=genre                 
            )
            book.save()
    return HttpResponse(b"CREATED DATABASE", status=201)

def get_book(request):
    books = MyMainBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', books))

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        display_title = max_title(title)
        authors = request.POST  .get("authors")
        image = request.POST.get("image")
        description = request.POST.get("description")
        isbn = request.POST.get("isbn")
        user = request.user

        new_book = MyMainBook(
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

def show_book_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def search_books(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get('query')

            # Debug: Cetak query untuk memastikan isi query
            print(f"Query: {query}")

            response = requests.post(
                'https://octopus-app-cvv6j.ondigitalocean.app/AI_Search',
                headers={'Content-Type': 'application/json'},
                json={'context': query}
            )

            # Debug: Cetak status code dan response untuk memeriksa hasil
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")

            if response.status_code == 200:
                books_data = response.json()
                return JsonResponse({'books': books_data.get('books', [])})
            else:
                return JsonResponse({'error': 'Error with external book API'}, status=response.status_code)

        except Exception as e:
            print(f"Exception: {e}")  # Debug: Cetak exception jika terjadi
            return JsonResponse({'error': str(e)}, status=500)
        
    return HttpResponseNotFound()