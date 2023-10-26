from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

# Create your views here.
def show_main(request):
    context = {
        'name': 'Testing',
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
    query = "romance"
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

def show_list(request):
    books = Book.objects.all() 

    context = {
        'books': books,
    }
    return render(request, "list.html", context)