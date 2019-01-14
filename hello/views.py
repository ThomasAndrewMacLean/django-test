from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts
# Create your views here.

def myView(request):
    return HttpResponse('Ann Verdonck, I love you!')


def homePage(request):
    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }

    return render(request, 'home/index.html',context)


def detailView(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'home/detail.html', context)
