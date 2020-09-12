---
title: About Me
styles:
    - about.css
---

<h1>About Me</h1>
<div id="resume">
    <div class="vertical-separator"></div>
    <span>If you would like to download the full resume, click
        <a class="text-based-link" href="/assets/docs/resume.pdf">
            HERE.
        </a>
    </span>
</div>


<section id="introduction">
<figure aria-label="James playing the bass in a suit" class="image"></figure>
<ul id="key-details">
    <li><strong class="key">Name: </strong>James Menzies</li>
    <li><strong class="key">Age: </strong>32</li>
    <li><strong class="key">Email: </strong>james.r.menzies@gmail.com</li>
    <li><strong class="key">Phone: </strong>(+61) 0432 801 574</li>
    <li><strong class="key">Location: </strong>Hobart, Tasmania, Australia</li>
</ul>
</section>

<section id="sales-pitch">
    <div id="nutshell">
        <h2>In a Nutshell...</h2>
        <p>{{ site.data.text["sales_pitch"] }}</p>
    </div>
    <div id="skills">
        <h2>Skills</h2>
        <ul class="flex-container">
            {% for skill in site.data.skills %}
            <li>{{ skill }}</li>
            {% endfor %}
        </ul>

    </div>
</section>

<section id="biography">
    <h2>Biography</h2>

    {% for paragraph in site.data.text["biography"] %}
    <p>{{ paragraph }}</p>
    {% endfor %}
</section>