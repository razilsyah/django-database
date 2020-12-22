from django.shortcuts import render

# Create your views here.

from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'judul': 'Home Blog',
        'postingan': posts
    }
    return render(request, 'index.html', context)


def berita(request):
    posts = Post.objects.filter(category='berita')
    context = {
        'judul': 'Home Blog',
        'postingan': posts
    }
    return render(request, 'index.html', context)


def gosip(request):
    posts = Post.objects.filter(category='gosip')
    context = {
        'judul': 'Home Blog',
        'postingan': posts
    }
    return render(request, 'index.html', context)
