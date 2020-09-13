---
title: Home
styles:
    - index.css
page_wrapper: true
---

<div id="mobile-only-banner" class="image"></div>

<section id="job-title">
    <span>BACK-END DEVELOPER</span>
    <div class="horizontal-divider image"></div>
    <span>CLASSICAL DOUBLE BASS PLAYER</span>
</section>

<div id="page-separator"></div>

<section id="welcome">
    <figure class="image" aria-label="A head shot of James grinning."></figure>
    <figcaption>{{ site.data.text["welcome_tag"] }}</figcaption>
</section>

<section id="directory">
    {% for directory in site.data.directories %}
    <a href={{ directory.url }} aria-label={{ directory.image_description }}
        class="directory-wrapper block-based-link">
        <h3>{{ directory.title }}</h3>
        <figure class="image" id={{ directory.id }}></figure>
        <figcaption>{{ directory.prompt }}</figcaption>
        </a>
    {% endfor %}
</section>