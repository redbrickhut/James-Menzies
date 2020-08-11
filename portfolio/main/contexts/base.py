# menu items

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

context = {
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

