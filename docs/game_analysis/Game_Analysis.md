---
title: Game Analysis
notebook: header
notebook-head: game_analysis
nav_order: 4
has_children: true
---

<ul>
{% for post in site.pages reversed %}
{% if post.notebook == page.notebook-head %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ul>