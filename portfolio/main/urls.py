from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('media', views.media, name='media'),
    path('blog', views.blog, name='blog'),
    path('<int:post_id>/blogposts', views.blogposts, name='blogposts'),
]