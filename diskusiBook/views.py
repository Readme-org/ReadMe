from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from main.views import Book
from .models import Comment, Post, Reply
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

def get_post_json(request, id):
    book = get_object_or_404(Book, id=id)
    posts = Post.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', posts))

def get_comment_json(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    return HttpResponse(serializers.serialize('json', comments))

def get_reply_json(request, id):
    comment = get_object_or_404(Comment, id=id)
    replies = Reply.objects.filter(comment=comment)
    return HttpResponse(serializers.serialize('json', replies))

def get_single_post_json(request, id):
    post = Post.objects.filter(id=id)
    return HttpResponse(serializers.serialize('json', post))

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
    book = get_object_or_404(Book, id=post.book.pk)
    comments = Comment.objects.filter(post=post)
        
    context = {
        'post': post,
        'book': book,
        'comments': comments,
        'name': request.user.username,
    }
    return render(request, 'post.html', context)


def show_json(request):
    data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_comment(request):
    data = Comment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_reply(request):
    data = Reply.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_username(request, user_id):
  try:
    user = User.objects.get(pk=user_id)
    return JsonResponse({'username': user.username})
  except User.DoesNotExist:
    raise Http404("User does not exist")

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

@csrf_exempt
def create_post_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_post = Post.objects.create(
            user = request.user,
            title = data["title"],
            content = data["content"],
            book = get_object_or_404(Book, id=data["book"]),
        )

        new_post.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

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
def remove_post_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post = get_object_or_404(Post, pk=data["post"], user=request.user)
        post.delete()
        return JsonResponse({"status": "success", "message": "Post telah berhasil dihapus."}, status=201)
    return JsonResponse({"status": "error", "message": "Terdapat kesalahan. Silahkan coba lagi."}, status=404)

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

@login_required(login_url='main:login')
@csrf_exempt
def edit_post_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        post = get_object_or_404(Post, pk=data["post"], user=request.user)
        post.title = data["title"]
        post.content = data["content"]

        post.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@login_required(login_url='main:login')
@csrf_exempt
def create_comment(request, id):
    if request.method == "POST":
        comment_text = request.POST.get('Commentcontent')
        post = get_object_or_404(Post, pk=id)

        comment = Comment.objects.create(
            post=post,
            user=request.user, 
            content=comment_text,
        )

        comment.save()
    
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def create_comment_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_comment = Comment.objects.create(
            user = request.user,
            content = data["content"],
            post = get_object_or_404(Post, id=data["post"]),
        )

        new_comment.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='main:login')
@csrf_exempt
def remove_comment(request, id):
    if request.method == "GET":
        comment = get_object_or_404(Comment, pk=id, user=request.user)
        comment.delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='main:login')
@csrf_exempt
def remove_comment_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        comment = get_object_or_404(Comment, pk=data["comment"], user=request.user)
        comment.delete()
        return JsonResponse({"status": "success", "message": "Comment telah berhasil dihapus."}, status=201)
    return JsonResponse({"status": "error", "message": "Terdapat kesalahan. Silahkan coba lagi."}, status=404)

@login_required(login_url='main:login')
@csrf_exempt
def edit_comment(request, id):
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=id, user=request.user)
        comment.content = request.POST.get("CommentEditcontent")
        comment.save()
        return HttpResponse(b"EDITED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='main:login')
@csrf_exempt
def edit_comment_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        comment = get_object_or_404(Comment, pk=data["comment"], user=request.user)
        comment.content = data["content"]

        comment.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='main:login')
@csrf_exempt
def create_reply(request, id):
    if request.method == "POST":
        reply_text = request.POST.get('Replycontent')
        comment = get_object_or_404(Comment, pk=id)

        reply = Reply.objects.create(
            comment=comment,
            user=request.user, 
            content=reply_text,
        )

        reply.save()
    
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def create_reply_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_reply = Reply.objects.create(
            user = request.user,
            content = data["content"],
            comment = get_object_or_404(Comment, id=data["comment"]),
        )

        new_reply.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='main:login')
@csrf_exempt
def remove_reply(request, id):
    if request.method == "GET":
        reply = get_object_or_404(Reply, pk=id, user=request.user)
        reply.delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='main:login')
@csrf_exempt
def remove_reply_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        reply = get_object_or_404(Reply, pk=data["reply"], user=request.user)
        reply.delete()
        return JsonResponse({"status": "success", "message": "Reply telah berhasil dihapus."}, status=201)
    return JsonResponse({"status": "error", "message": "Terdapat kesalahan. Silahkan coba lagi."}, status=404)

@login_required(login_url='main:login')
@csrf_exempt
def edit_reply(request, id):
    if request.method == "POST":
        reply = get_object_or_404(Reply, pk=id, user=request.user)
        reply.content = request.POST.get("ReplyEditcontent")
        reply.save()
        return HttpResponse(b"EDITED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='main:login')
@csrf_exempt
def edit_reply_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        reply = get_object_or_404(Reply, pk=data["reply"], user=request.user)
        reply.content = data["content"]

        reply.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)