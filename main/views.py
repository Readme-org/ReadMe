from django.http import HttpResponse
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
    query = "random"
    books_data = fetch_books(query, 40)

    # Potong setiap judul buku
    for book_data in books_data:
        title = book_data['volumeInfo']['title']
        authors = ", ".join(book_data['volumeInfo'].get('authors', []))
        image = book_data['volumeInfo']['imageLinks']['thumbnail']
        

        book = Book(
            title=title,
            display_title=max_title(title),
            authors=authors,
            image=image,
        )
        book.save()
    return HttpResponse(b"CREATED", status=201) 

