from django.db import models


class Author(models.Model):
    pass



class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    snippet = models.TextField()
    author = models.ForeignKey(Author)
    content = models.TextField()



class ExternalLink:

    def __init__(self, icon_url, url):
        self.url = url
        self.icon_url = icon_url


class InternalLink:

    def __init__(self, title, url):
        self.title = title
        self.url = url


class Image:

    def __init__(self, url, caption):
        self.url = url
        self.caption = caption


class Directory:

    def __init__(self, title, image, url, prompt):
        self.title = title
        self.image = image
        self.prompt = prompt
        self.url = url
