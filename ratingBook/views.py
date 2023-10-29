from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import Rating, Book

# Create your views here.
def show_rating(request):
    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'rating.html', context)

def show_rating_to_update(request, id):
    book = Book.objects.get(id=id)
    rating = Rating.objects.get(book_id=id)

    context = {
        'book': book,
        'rating': rating
    }

    return render(request, 'update_rating.html', context)

def get_rating_json(request, id):
    ratings = Rating.objects.filter(book_id=id)
    
    data = serializers.serialize('json', ratings)
    
    return HttpResponse(data, content_type='application/json')

@login_required(login_url='main:login')
def create_rating_ajax(request):
    if request.method == 'POST':
        user = request.user
        book_id = request.POST['book']
        book = Book.objects.get(id=book_id)
        rating = request.POST['rating']
        message = request.POST['message']

        rating = Rating.objects.create(user=user, book=book, rating=rating, message=message)
        
        return HttpResponse('Rating created successfully', status=201)
    return HttpResponseForbidden('Allowed only via POST')

@login_required(login_url='main:login')
def update_rating_ajax(request):
    if request.method == 'POST':
        user = request.user
        book_id = request.POST['book']
        rating = request.POST['rating']
        message = request.POST['message']

        rating = Rating.objects.filter(user=user, book_id=book_id).update(rating=rating, message=message)
        
        return HttpResponse('Rating updated successfully', status=201)
    return HttpResponseForbidden('Allowed only via POST')

@login_required(login_url='main:login')
def delete_rating(request, id):
    rating = Rating.objects.get(id=id)
    if request.user == rating.user:
        rating.delete()
        return redirect('ratingBook:show_rating')
    return HttpResponseForbidden('You are not allowed to delete this rating')
