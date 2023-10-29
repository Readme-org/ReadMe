from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404
from main.views import Book
from .models import Comment, Post, Reply
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

def get_post_json(request, id):
    book = get_object_or_404(Book, id=id)
    posts = Post.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', posts))

def show_discussion(request, id): 
    book = get_object_or_404(Book, id=id)
    posts = Post.objects.filter(book=book)

#     context = {
#         'posts': posts,
#         'book': book,
#         'name': request.user.username,
#     }

#     return render(request, "thread.html", context)

@login_required(login_url='main:login')
@csrf_exempt
def show_post(request, title): #book id
    post = get_object_or_404(Post, title=title)
    comments = Comment.objects.filter(post=post)

#     if "comment-form" in request.POST: # comment-form is name of html element
#         comment = request.POST.get("comment") # name="comment" as html attribute
#         new_comment, created = Comment.objects.get_or_create(user=request.user, content=comment, post=post)
#         post.comments.add(new_comment.id)
#     if "reply-form" in request.POST: # reply-form is name of html element
#         reply = request.POST.get("reply") # name="reply" as html attribute
#         comment_id = request.POST.get("comment-id") # ??????
#         comment_obj = Comment.objects.get(id=comment_id)
#         new_reply, created = Reply.objects.get_or_create(user=request.user, content=reply, comment=comment_obj)
#         comment_obj.replies.add(new_reply.id)
        
    context = {
        'post': post,
        'comments': comments,
        'name': request.user.username,
    }
    return render(request, 'post.html', context)

# @login_required(login_url='main:login')
# @csrf_exempt
# def create_post(request, book_id):
#     form = PostForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         title = request.Post.get("title")
#         content = request.Post.get("content")
#         user = request.user
#         book = Book.objects.get(id=book_id)
#         new_post = Post(book=book, title=title, user=user, content=content)
#         new_post.save()
#         return HttpResponse(b"CREATED", status=201)

#     return HttpResponseNotFound()

# @property
# def last_reply(self):
#     return self.comments.latest("date")
# @property
# def last_reply(self):
#     return self.comments.latest("date")
