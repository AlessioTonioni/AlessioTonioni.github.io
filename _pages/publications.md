---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<h2 style="border-bottom: 2px solid #eaeaea; padding-bottom: 10px; margin-top: 20px; color: #2c3e50; font-size: 1.8em;">Under Review Articles</h2>
{% for post in site.publications reversed %}
  {% if post.pubtype == 'review' %}
      {% include archive-publication-card.html %}
  {% endif %}
{% endfor %}

<h2 style="border-bottom: 2px solid #eaeaea; padding-bottom: 10px; margin-top: 50px; color: #2c3e50; font-size: 1.8em;">Conference Papers</h2>
{% for post in site.publications reversed %}
  {% if post.pubtype == 'conference' %}
      {% include archive-publication-card.html %}
  {% endif %}
{% endfor %}

<h2 style="border-bottom: 2px solid #eaeaea; padding-bottom: 10px; margin-top: 50px; color: #2c3e50; font-size: 1.8em;">Journal Articles</h2>
{% for post in site.publications reversed %}
  {% if post.pubtype == 'journal' %}
      {% include archive-publication-card.html %}
  {% endif %}
{% endfor %}


