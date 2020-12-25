from django.shortcuts import render

# Create your views here.
# agar class model di tampilkan di html
from .models import Post


def Index(request):
    Posts = Post.objects.all()
    print(Post)

    categories = Post.objects.values('category').distinct()
    context = {
        'judul': 'Home Blog',
        'posts': Posts,
        'categories': categories
    }
    return render(request, 'blog/index.html', context)


def CategoryPost(request, categoryInput):
    Posts = Post.objects.filter(category=categoryInput)

    # untuk mengambil category unik
    categories = Post.objects.values('category').distinct()

    context = {
        'judul': 'Berdasarkan category',
        'content': 'tampilkan berdasarkan category',
        'posts': Posts,
        'categories': categories
    }
    return render(request, 'blog/category.html', context)


def DetailPost(request, slugInput):
    Posts = Post.objects.get(slug=slugInput)

    categories = Post.objects.values('category').distinct()
    context = {
        'judul': 'POST',
        'categories': categories,
        'posts': Posts
    }
    return render(request, 'blog/detail.html', context)
