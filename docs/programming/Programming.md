---
title: Programming
notebook: header
notebook-head: programming
nav_order: 3
has_children: true
has_toc: false
---

<ul>
{% for post in site.pages %}
{% if post.notebook == page.notebook-head %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ul>