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
    {% for detail in site.data.key_details %}
    <li><strong class="key">{{ detail["metric"] }}: </strong>{{ detail["value"] }}</li>
    {% endfor %}
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