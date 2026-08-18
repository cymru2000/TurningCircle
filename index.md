---
layout: base.njk
title: "Turning Circle | Built for the journey"
---

We focus on the adventure, the road trips, and the stories—not just the spec sheets. 

## Latest Adventures

<ul>
{% for post in collections.adventures %}
  <li>
    <strong><a href="{{ post.url }}">{{ post.data.title }}</a></strong> 
    <br>
    <em>Published on {{ post.date | date: "%Y-%m-%d" }}</em>
  </li>
{% endfor %}
</ul>