---
title: Table of Contents
layout: home
nav_order: 1
has_children: false
---
<br>
<h1 style="font-size: 3rem !important;" id="page-title">Table of Contents</h1>

<h1>
    <a href="/docs/engineering/Engineering.html"> Engineering </a> -
</h1>

<ol>
{% for post in site.pages %}
{% if post.notebook == "engineering" %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ol>

<h1>
    <a href="/docs/programming/Programming.html"> Programming </a> -
</h1>

<ol>
{% for post in site.pages %}
{% if post.notebook == "programming" %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ol>

<h1>
    <a href="/docs/game_analysis/Game_analysis.html"> Game Analysis </a> -
</h1>

<ol>
{% for post in site.pages %}
{% if post.notebook == "game_analysis" %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ol>

<h1>
    <a href="/docs/skills_history/Skills_History.html"> Skills History </a> -
</h1>

<ol>
{% for post in site.pages %}
{% if post.notebook == "skills_history" %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ol>

<h1>
    <a href="/docs/team_meetins/team_history.html"> Team History </a> -
</h1>

<ol>
{% for post in site.pages %}
{% if post.notebook == "team_history" %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ol>

<h1>
    <a href="/docs/research/Research.html"> Research </a> -
</h1>

<ol>
{% for post in site.pages %}
{% if post.notebook == "research" %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ol>

<h1>
    <a href="/docs/tournament_history/TournamentHistory.html"> Tournament History </a> -
</h1>

<ol>
{% for post in site.pages %}
{% if post.notebook == "TournamentHistory" %}
    <li>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> 
    - {{ post.date | date: "%B %d, %Y" }}
    </li>
{% endif %}
{% endfor %}
</ol>
