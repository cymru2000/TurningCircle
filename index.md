---
layout: base.njk
title: "Turning Circle | Built for the journey"
---

TurningCircle covers the UK car market and the switch to electric, with researched guides and the stories behind the spec sheets.

## Latest Articles

<ul>
{% for post in collections.posts %}
  <li>
    <strong><a href="{{ post.url }}">{{ post.data.title }}</a></strong>
    <br>
    <em>Published on {{ post.date | date: "%Y-%m-%d" }}</em>
  </li>
{% endfor %}
</ul>
