# menu items

class ExternalLink:

    def __init__(self, url, icon_url):
        self.icon_url = icon_url
        self.url = url

class InternalLink:

    def __init__(self, title, url):
        self.title = title
        self.url = url


context = {
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

