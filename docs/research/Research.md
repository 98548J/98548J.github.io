---
title: Research
notebook: header
notebook-head: research
nav_order: 7
has_children: true
---

<ul>
{% for post in site.pages reversed%}
{% if post.notebook == page.notebook-head %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ul>