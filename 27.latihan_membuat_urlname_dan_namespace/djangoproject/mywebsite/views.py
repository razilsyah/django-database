from django.shortcuts import render


def index(request):
    context = {
        'judul': 'Home Page'
    }
    return render(request, 'index.html', context)
