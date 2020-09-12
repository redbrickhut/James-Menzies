---
title: Media
styles:
  - media.css
---

<h1>Media</h1>
<section id="introduction">
        <p>{{ site.data.text["media_intro"] }}</p>
        <span>For the personal side of things, my Instagram is right
                    <a class="text-based-link" target="_blank" href="https://www.instagram.com/redbrickhut/">
                        HERE.
                    </a>
        </span>
</section>


<section id="videos">
    <h2>Videos</h2>

    {% assign media_links = site.media_links | sort: "date_posted" | reverse %}
    {% for media_link in media_links %}
    <figure>
        <iframe src="{{ media_link.link }}" aria-labelledby="tso-video"
                frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>

        </iframe>
        <figcaption class="video-summary">
            {{ media_link.content }}
        </figcaption>
    </figure>
    {% endfor %}
 
</section>
