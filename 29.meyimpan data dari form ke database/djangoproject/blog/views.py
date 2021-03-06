from django.shortcuts import render, redirect

# from django.http import HttpResponseRedirect
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
    # request.POST or None adalah validation memberitahukan bahwa form tsb harus diisi
    post_form = PostForm(request.POST or None)
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()
            return redirect('blog:index')
    context = {
        'page_title': 'CREATE',
        'post_form': post_form
    }
    return render(request, 'blog/create.html', context)
