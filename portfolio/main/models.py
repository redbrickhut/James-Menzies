from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='authors')

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    snippet = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    content = models.TextField()
    pub_date = models.DateField(default=timezone.now)
    tags = models.ManyToManyField(Tag, blank=True)

    def get_tags_as_str(self):
        tags = [str(tag) for tag in self.tags.all()]
        return ", ".join(tags)

    def __str__(self):
        return self.title


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
