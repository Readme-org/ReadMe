from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .models import Rating, Book
from django.core import serializers

# Create your views here.
@login_required(login_url='main:login')
def show_rating(request):
    books = Book.objects.all()

    context = {
        'books': books,
        'name': request.user.username,
    }

    return render(request, 'rating.html', context)

@login_required(login_url='main:login')
def show_rating_to_update(request, id):
    review = Rating.objects.get(id=id)
    book = Book.objects.get(id=review.book_id)

    if request.user != review.user:
        return HttpResponseForbidden('You are not allowed to update this rating')

    context = {
        'book': book,
        'review': review
    }

    return render(request, 'update.html', context)

def get_rating_json(request, id):
    ratings = Rating.objects.filter(book_id=id)

    data = []
    for rating in ratings:
        rating_dict = model_to_dict(rating)
        rating_dict['username'] = rating.user.username
        data.append(rating_dict)

    return JsonResponse(data, safe=False)

@login_required(login_url='main:login')
def create_rating_ajax(request):
    if request.method == 'POST':
        print(request.POST)
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

def show_rating_json(request):
    data = Rating.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")