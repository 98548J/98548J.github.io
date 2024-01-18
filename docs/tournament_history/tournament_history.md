---
title: Tournament History
notebook: header
notebook-head: Tournament History
nav_order: 8
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