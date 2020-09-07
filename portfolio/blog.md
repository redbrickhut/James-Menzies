---
title: blog
styles: 
  - blog.css
---

<h1>Blog</h1>
<section id="introduction">
    <p>
        When I'm working on a project, I find it is often helpful to document solutions as I
        stumble across them. Other times I just like to think out loud. Here are those thoughts...
        I hope there's something here that helps you out too. If not, I promise to make the
        diversion entertaining.
    </p>
    <figure id="blog-photo" aria-label="James pausing at the whiteboard
    to take a sip of a delicious beverage" class="image"></figure>
</section>


<section id="contents">

{% for post in site.posts %}
{% assign author = site.data.authors[post.author] %}
<a href="{{ post.url }}" class="post block-based-link">
    <div class="details">
        <h2>{{ post.title }}</h2>
        <span class="publish-date"><strong class="key">Date: </strong>{{ post.date | date: "%d/%m/%Y" }}</span>
        <span class="author"><strong class="key">Author: </strong>{{ author.name }}</span>
        <span class="tags"><strong class="key">Tags: </strong> {{ post.tags | join: ', ' }}</span>
    </div>
    <p>
    This is the excerpt of the blog post.
    </p>
    <div class="image arrow-button"></div>
{% endfor %}
</a>

</section>
