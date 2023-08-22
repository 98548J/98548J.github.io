---
title: Skills History
notebook: header
notebook-head: skills_history
nav_order: 5
has_children: true
has_toc: false
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