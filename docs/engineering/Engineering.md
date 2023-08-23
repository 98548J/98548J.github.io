---
title: Engineering
notebook: header
notebook-head: engineering
nav_order: 2
has_children: true
has_toc: false
---

<ol>
{% for post in site.pages %}
{% if post.notebook == page.notebook-head %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ol>

