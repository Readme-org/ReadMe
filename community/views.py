from django.shortcuts import render
from main.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-votes')
    return render(request, 'home.html', {'posts':posts})