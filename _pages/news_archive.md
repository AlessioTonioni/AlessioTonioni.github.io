---
layout: single
title: "News Archive"
permalink: /news/
author_profile: true
---

<style>
  .news-container {
    margin-top: 20px;
    border-left: 2px solid #3498db;
    padding-left: 20px;
  }
  .news-item {
    margin-bottom: 30px;
    position: relative;
  }
  .news-item::before {
    content: '';
    position: absolute;
    left: -29px;
    top: 5px;
    width: 15px;
    height: 15px;
    background: #3498db;
    border: 3px solid #fff;
    border-radius: 50%;
  }
  .news-date {
    font-size: 0.85em;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 5px;
    display: block;
  }
  .news-content {
    font-size: 1.1em;
    line-height: 1.5;
  }
  .news-content p {
    margin: 0;
  }
  .year-header {
    margin-top: 40px;
    margin-bottom: 20px;
    color: #3498db;
    font-weight: bold;
    border-bottom: 1px solid #eee;
    padding-bottom: 5px;
  }
</style>

<div class="news-container">
{% assign news_sorted = site.data.news | sort: "date" | reverse %}
{% assign last_year = "" %}

{% for item in news_sorted %}
  {% assign current_year = item.date | date: "%Y" %}
  {% if current_year != last_year %}
    <h2 class="year-header">{{ current_year }}</h2>
    {% assign last_year = current_year %}
  {% endif %}

  <div class="news-item">
    <span class="news-date">{{ item.date | date: "%B %d, %Y" }}</span>
    <div class="news-content">
      {{ item.content | markdownify }}
    </div>
  </div>
{% endfor %}
</div>
