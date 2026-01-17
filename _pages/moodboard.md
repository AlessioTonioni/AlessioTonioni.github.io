---
layout: single
title: "Moodboard"
permalink: /moodboard/
author_profile: true
---

A collection of photography and soundtracks that inspire me.

<style>
  .mood-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 25px;
    margin-top: 30px;
  }
  .mood-card {
    background: #fff;
    border: 1px solid #eee;
    border-radius: 12px;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
  }
  .mood-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.05);
  }
  .mood-image-container {
    width: 100%;
    aspect-ratio: 4 / 3;
    overflow: hidden;
    background: #f0f0f0;
  }
  .mood-image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
  }
  .mood-card:hover .mood-image-container img {
    transform: scale(1.05);
  }
  .mood-info {
    padding: 15px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .mood-title {
    font-size: 1.1em;
    font-weight: bold;
    margin-bottom: 5px;
    color: #333;
  }
  .mood-desc {
    font-size: 0.9em;
    color: #666;
    margin-bottom: 15px;
    line-height: 1.4;
  }
  .mood-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #f5f5f5;
    padding-top: 10px;
    font-size: 0.8em;
  }
  .mood-date {
    color: #999;
  }
  .mood-link {
    color: #e74c3c;
    text-decoration: none;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 5px;
  }
  .mood-link:hover {
    color: #c0392b;
  }
</style>

<div class="mood-grid">
{% for mood in site.data.moods %}
  <div class="mood-card">
    {% if mood.image %}
    <div class="mood-image-container">
      <img src="{{ mood.image | relative_url }}" alt="{{ mood.title }}" loading="lazy">
    </div>
    {% endif %}
    <div class="mood-info">
      <div>
        <div class="mood-title">{{ mood.title }}</div>
        <div class="mood-desc">{{ mood.description }}</div>
      </div>
      <div class="mood-meta">
        <span class="mood-date">{{ mood.date | date: "%B %Y" }}</span>
        {% if mood.youtube_id %}
        <a href="https://www.youtube.com/watch?v={{ mood.youtube_id }}" target="_blank" class="mood-link">
          <i class="fas fa-play-circle"></i> Listen
        </a>
        {% endif %}
      </div>
    </div>
  </div>
{% endfor %}
</div>
