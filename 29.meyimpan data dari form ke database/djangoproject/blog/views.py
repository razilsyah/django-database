from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import PostForm
from .models import PostModel


def index(request):
    posts = PostModel.objects.all()
    context = {
        'page_title': 'postingan blog',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def create(request):
    post_form = PostForm()
    print(request.POST)

    if request.method == 'POST':
        PostModel.objects.create(
            judul=request.POST.get('judul'),
            body=request.POST.get('body'),
            category=request.POST.get('category')
        )
        return HttpResponseRedirect("/blog/")
    context = {
        'page_title': 'CREATE',
        'post_form': post_form
    }
    return render(request, 'blog/create.html', context)
