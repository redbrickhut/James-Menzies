from django.shortcuts import render
from .contexts import base
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = base.context
    context['title'] = "Home"
    return render(request, 'main/base.html', context)


def about(request):
    return HttpResponse("About Page")


def projects(request):
    return HttpResponse("My Projects")


def media(request):
    return HttpResponse("Meida")


def blog(request):
    return HttpResponse("Blogs")
