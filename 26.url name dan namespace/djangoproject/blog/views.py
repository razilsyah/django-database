from django.shortcuts import render

# Create your views here.


def Khusus(request, input):
    context = {
        'judul': input,
    }

    return render(request, 'blog/index.html', context)


def CategoryPost(request):
    context = {
        'judul': 'Category Post',
    }

    return render(request, 'blog/index.html', context)


def SinglePost(request):
    context = {
        'judul': 'Single Post',
    }

    return render(request, 'blog/index.html', context)


def index(request):
    context = {
        'judul': 'Home Blog',
    }

    return render(request, 'blog/index.html', context)
