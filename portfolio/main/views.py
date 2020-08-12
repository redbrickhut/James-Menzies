from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .text import *
from .images import *

# Create your views here.
base_context = {
    "menu_icon": "menu.png",
    "int_links": [
        InternalLink("Home", "index"),
        InternalLink("About Me", "about"),
        InternalLink("My Projects", "projects"),
        InternalLink("Media", "media"),
        InternalLink("Blog", "blog")

    ],
    "ext_links": [
        ExternalLink('github.png', 'https://github.com/redbrickhut'),
        ExternalLink('instagram.png', 'https://www.instagram.com/redbrickhut/'),
        ExternalLink('linkedin.png', 'https://www.linkedin.com/in/james-menzies-24ab3a184/'),
        ExternalLink('mail.png', 'mailto:james.r.menzies@gmail.com'),
    ]
}


def index(request):
    context = base_context
    context['title'] = "Home"
    context['page_wrapper'] = True
    context['welcome_message'] = welcome_message
    context['directories'] = [
        Directory("The Person", tso_headshot, 'about', person_directory_prompt),
        Directory("The Coder", computer_shot, 'projects', coder_directory_prompt),
        Directory("The Musician", musician_shot, 'media', musician_directory_prompt),
    ]

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse("About Page")


def projects(request):
    return HttpResponse("My Projects")


def media(request):
    return HttpResponse("Media")


def blog(request):
    return HttpResponse("Blogs")
