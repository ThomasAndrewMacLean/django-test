from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myView(request):
    return HttpResponse('Hello World!')


def homePage(request):
    return HttpResponse('Home Pageeeee')