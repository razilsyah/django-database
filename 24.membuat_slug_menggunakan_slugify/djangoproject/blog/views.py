# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Post


def index(request):

    heading = '<h1> Home Blog </h1>'
    return HttpResponse(heading)


def categoryPost(request, categoryInput):

    posts = Post.objects.filter(category=categoryInput)
    print(posts)
    return HttpResponse(Post.judul)


def singlePage(request, input):
    # karna slug itu unik tidak boleh ada yang sama karna mengacu pada judul
    posts = Post.objects.get(slug=input)

    judul = '<h1>{}</h1>'.format(posts.judul)
    body = '<h1>{}</h1>'.format(posts.body)
    category = '<h1>{}</h1>'.format(posts.category)

    return HttpResponse(judul + body + category)
