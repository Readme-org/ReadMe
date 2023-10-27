from django.shortcuts import redirect, render, get_object_or_404
from main.views import Book
from .models import Comment, Post, Reply
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def show_diskusi(request, id):
    book = Book.objects.get(pk=id)

    context = {
        "book": book,
    }

    return render(request, "diskusi.html", context)


def show_thread(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if "comment-form" in request.POST: # comment-form is name of html element
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=request.user, content=comment)
        post.comments.add(new_comment.id)
    if "reply-form" in request.POST: # reply-form is name of html element
        reply = request.POST.get("reply")
        comment_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=comment_id)
        new_reply, created = Reply.objects.get_or_create(user=request.user, content=reply)
        comment_obj.replies.add(new_reply.id)

    context = {
        "post": post,
    }

    return render(request, "diskusi.html", context)


def show_posts(request):
    posts = Post.objects.filter(pk=id)  # Book id

    context = {
        "posts": posts,
    }

    return render(request, "diskusi.html", context)


@login_required
def create_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_post = form.save(commit=False)
        new_post.user = request.user
        new_post.save()
        return redirect("diskusi")
    context = {
        "form": form,
        "title": "Create new Post",
    }
    return render(request, "diskusi.html", context)

@property
def last_reply(self):
    return self.comments.latest("date")
