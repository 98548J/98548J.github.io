---
title: Team Meetings
notebook: header
notebook-head: team_meetings
nav_order: 6
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