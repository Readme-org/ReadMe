from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import Rating

# Create your views here.
def debug(request):
    return render(request, 'book_rating.html')

def show_rating(request, id):
    ratings = Rating.objects.filter(book_id=id)
    
    context = {
        'ratings': ratings
    }
    
    return render(request, 'book_rating.html', context)

def get_rating_json(request, id):
    ratings = Rating.objects.filter(book_id=id)
    
    data = serializers.serialize('json', ratings)
    
    return HttpResponse(data, content_type='application/json')

@login_required(login_url='main:login')
def create_rating_ajax(request):
    if request.method == 'POST':
        user = request.user
        book_id = request.POST['book_id']
        rating = request.POST['rating']
        description = request.POST['description']
        
        Rating.objects.create(
            user=user,
            book_id=book_id,
            rating=rating,
            description=description
        )
        
        return HttpResponse('Rating created successfully', status=201)
    return HttpResponseForbidden('Allowed only via POST')

@login_required(login_url='main:login')
def update_rating_ajax(request):
    if request.method == 'POST':
        user = request.user
        book_id = request.POST['book_id']
        rating = request.POST['rating']
        description = request.POST['description']
        
        rating = Rating.objects.get(user=user, book_id=book_id)
        rating.rating = rating
        rating.description = description
        rating.save()
        
        return HttpResponse('Rating updated successfully', status=201)
    return HttpResponseForbidden('Allowed only via POST')

@login_required(login_url='main:login')
def delete_rating_ajax(request):
    if request.method == 'POST':
        user = request.user
        book_id = request.POST['book_id']
        
        rating = Rating.objects.get(user=user, book_id=book_id)
        rating.delete()
        
        return HttpResponse('Rating deleted successfully', status=201)
    return HttpResponseForbidden('Allowed only via POST')
