---
title: Research
notebook: header
notebook-head: research
nav_order: 7
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