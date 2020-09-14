# Portfolio for James Menzies

## Target Audience

Given my background as a professional musician, I have a rare opportunity to corner an area of the market that most programmers don't. This namely being musicians who are in need of a developer, but also require someone who has a knowledge of the nuances and jargon of the musical profession as well.

Whilst the intention is to optimize my website towards this demographic, I am mindful to make sure that it caters towards all potential employers as well.

## Purpose of Website

There are four core purposes of this website:
1. I want to make it as efficient as possible for employers to find my credentials and contact details.
2. I want to showcase my work in a more interactive way than is possible with a standard Github repository. I also want to cater to those that might feel apprehensive about visiting Github as well.
3. I want to demonstrate my capabilities through the working integrity of the website.
4. I want to showcase my life as a professional musician. The aim is to create a unique impression for those who aren't from my background, and to affirm my integrity to those that are.

## Functionality and Features

### The Navigation Shell

A big component of the design brief was to both create a uniform look and to create a responsive site layout with distinct mobile and desktop versions. No component plays a bigger role in this than the navigation shell due to its sheer presence on the screen. It has three distinct parts:

1. A header, which displays the name of the current page, as well as a menu button.
2. A menu, which allows the user to travel to a different page
3. A footer, which provides links to external websites (such as LinkedIn and Github pages).

It also has three distinct modes:

| Name | Width | Function |
| --- | --- | ---|
| Mobile | <600px | Menu is hidden by default, pressing the menu button will cause the menu to appear vertically. The effect is animated. | 
| Tablet | 600 - 950px | As above, but menu appears from the left hand side. |
|Desktop | >950px | Menu is always visible, menu button is disabled and removed. Icons are repositioned.

The rest of the display is complemented by a background image which is fixed in place, and then a slightly transparent content layer that scrolls, creating a parallax effect. As the screen widens, I restrict the pages content to a width of 950 pixels. This protects the layout of the page while allowing the interest of the backdrop behind to shine through. \
\
The implementation for all of this is contained in the styles.css and nav.css, allowing for easy reusability.

### Colour Scheme

Given that my website has extensive written content, I wanted to make sure that I found a colour scheme that would cause minimal eye strain. To that end I decided to go with two shades of off-black, as well as two shades of green which contrast nicely. I've utilized the lighter version of the green to draw the viewer to particular points of interest (such as links and headers). I have stored all of these colours in the root component of styles.css, so if I want to add colour schemes down the track it will be an efficient process.

### The Home Page

My main concern with the home page was to efficiently direct the user to the part of the site they wished to visit. The user is greeted with a simple welcome message, followed by graphical links to the "About Me", "My Projects" and "Media" pages. 

Once the screen widens past 600px, I wanted all of this information to displayed on the screen without any scrolling required. To achieve this, I used nested flex boxes, both horizontal and vertical, which mean that even wide but not tall displays can still manage to fit all of the page's content. The default page content dimensions have also been extensively overriden. 

On certain mediums (such as a MacBook Air not in full screen mode), the screen gets quite wide but has limited height. I've needed to unload some elements to retain the page's integrity.

### The About Page

I wanted to make sure that the resume was clearly visible, so I included it at the top of the page and made use of colouring to make it stand out. Another point of interest is the skills section, where I style list elements to create badge-like objects.

### Projects

I was aware that listing my projects had the potential to create a rather monotone experience, so I used some nth child pseudo selectors to reverse the layout design. 

### Media

The point of this page is to validate my credentials as a musician. Stylistically not too much is required, through I do use a flex box to dynamically resize the image components.

### Blogs

This is very similar in layout to the Projects page. One of the compromises I had to make was removing the teaser text for the post when scaling to the mobile design. Each post takes the user to a discrete page to read the article. For the post, one of the challenges was to get the small elements that comprise the introduction to align and render aesthetically.\


## Tech Stack
* HTML
* CSS
* Git
* Github
* Jekyll
