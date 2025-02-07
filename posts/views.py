from django.shortcuts import render
from django.http import HttpResponse
from posts.models import *

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {'posts':posts, 'title':"Hello isip28!"})

def authorization(request):
    return HttpResponse("<h1>Authorization</h1>")