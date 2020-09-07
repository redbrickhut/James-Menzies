---
title: Media
styles:
  - media.css
---

<h1>Media</h1>
<section id="introduction">
        <p>
            Here you will find various photos and videos of me taken throughout my career as a double bass player.
            Most of these are taken from rehearsals and performances with my orchestra the TSO.
            I have also collaborated with other local artists such as (permission pending).
            If you're a local artist based in Hobart and want to do something together,
            get in touch and we can a coffee and a chat!
        </p>
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
