from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from main.views import Book
from .models import Comment, Post, Reply
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

def get_post_json(request, id):
    book = get_object_or_404(Book, id=id)
    posts = Post.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', posts))

def show_discussion(request, id): 
    book = get_object_or_404(Book, id=id)
    posts = Post.objects.filter(book=book)

    context = {
        'posts': posts,
        'book': book,
        'name': request.user.username,
        'user_id': request.user.id
    }

    return render(request, "thread.html", context)

@login_required(login_url='main:login')
@csrf_exempt
def show_post(request, id):
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(post=post)
        
    context = {
        'post': post,
        'comments': comments,
        'name': request.user.username,
    }
    return render(request, 'post.html', context)

@login_required(login_url='main:login')
@csrf_exempt
def create_post(request, id):
    form = PostForm(request.POST or None)
    book = get_object_or_404(Book, id=id)

    if form.is_valid() and request.method == "POST":
        post = form.save(commit=False)
        post.user = request.user
        post.book = book
        post.save()
        return HttpResponseRedirect(reverse('diskusiBook:show_discussion', args=[id]))
    
    context = {'form': form, 'book': book}
    return render(request, "create_post.html", context)

@login_required(login_url='main:login')
@csrf_exempt
def remove_post(request, id):
    if request.method == "GET":
        post = get_object_or_404(Post, pk=id, user=request.user)
        post.delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='main:login')
@csrf_exempt
def edit_post(request, id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=id, user=request.user)
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return HttpResponse(b"EDITED", status=201)
    return HttpResponseNotFound()

    # form = PostForm(request.POST or None)
    # if request.method == "POST" and form.is_valid():
    #     title = request.Post.get("title")
    #     content = request.Post.get("content")
    #     user = request.user
    #     book = Book.objects.get(id=book_id)
    #     new_post = Post(book=book, title=title, user=user, content=content)
    #     new_post.save()
    #     return HttpResponse(b"CREATED", status=201)

    # return HttpResponseNotFound()

    # form = ItemForm(request.POST or None)

    # if form.is_valid() and request.method == "POST":
    #     item = form.save(commit=False)
    #     item.user = request.user
    #     item.save()
    #     return HttpResponseRedirect(reverse('main:show_main'))
    
    # context = {'form': form}
    # return render(request, "create_item.html", context)

# @property
# def last_reply(self):
#     return self.comments.latest("date")
