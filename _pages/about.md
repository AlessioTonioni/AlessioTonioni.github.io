---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hello!

I am an **AI Researcher** at **Google XR Zurich** in [Federico Tombari](https://federicotombari.github.io/)'s team. I lead my own applied research team focused on AI technologies for the current and next generation of XR devices. We work on the whole stack ranging from the integration of AI technologies to improving Gemini for egocentric assistant use cases.  

I earned my Ph.D. in Computer Science and Engineering from the **University of Bologna** in 2019 at the [Computer Vision Lab](https://www.vision.deis.unibo.it/), advised by Professor [Luigi Di Stefano](https://scholar.google.ch/citations?user=xZVTzyAAAAAJ&hl=de). 

My research journey began with deep learning for retail environments and depth estimation for autonomous driving. Since then, it has evolved through several different topics, ranging from implementing some of the visual translation stack powering Google Lens and Google translate to  different image understanding tasks without forgetting some of my early 3D reconstruction and generation works. My current focus is on **multimodal video/image understanding and generation** using LLMs and Diffusion models.

I'm always excited to discuss new ideas or explore emerging topics. If you find any of our work interesting, please don't hesitate to reach out! 

---
<div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 20px;">
  <a href="mailto:alessio.tonioni.91@gmail.com" class="btn btn--primary">Email Me</a>
  <a href="https://www.linkedin.com/in/alessio-tonioni-16261668" class="btn btn--info">LinkedIn</a>
  <a href="https://github.com/AlessioTonioni" class="btn btn--inverse">GitHub</a>
  <a href="https://scholar.google.it/citations?user=ry_BLFUAAAAJ&hl=en" class="btn btn--warning">Google Scholar</a>
</div>

---

<style>
  .news-container {
    margin-top: 20px;
    border-left: 2px solid #3498db;
    padding-left: 20px;
  }
  .news-item {
    margin-bottom: 20px;
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
    font-size: 1.05em;
    line-height: 1.5;
  }
  .news-content p {
    margin: 0;
  }
  .btn--light--outline {
    margin-top: 10px;
    display: inline-block;
  }
</style>

## 📢 Latest News

<div class="news-container">
{% assign latest_news = site.data.news | sort: "date" | reverse | slice: 0, 5 %}
{% for item in latest_news %}
  <div class="news-item">
    <span class="news-date">{{ item.date | date: "%B %Y" }}</span>
    <div class="news-content">
      {{ item.content | markdownify }}
    </div>
  </div>
{% endfor %}
</div>

[All News & Archive →]({{ '/news/' | relative_url }}){: .btn .btn--light--outline}

---

## 🎵 Current Mood

{% assign current_mood = site.data.moods | first %}

<div class="mood-spotlight" style="border: 1px solid #eee; padding: 20px; border-radius: 8px; background: #fafafa;">
  <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 20px; margin-bottom: 5px;">
    <div style="flex: 1;">
      <h3 style="margin-top: 0; margin-bottom: 5px;">{{ current_mood.title }}</h3>
      <p style="margin-bottom: 0;"><em>{{ current_mood.description }}</em></p>
    </div>
    {% if current_mood.youtube_id %}
    <div style="flex-shrink: 0;">
      <a href="https://www.youtube.com/watch?v={{ current_mood.youtube_id }}" target="_blank" class="btn btn--danger" style="margin: 0; display: flex; align-items: center; gap: 8px;">
        <i class="fas fa-play" aria-hidden="true"></i> Play Soundtrack
      </a>
    </div>
    {% endif %}
  </div>
  
  {% if current_mood.image %}
  <div style="width: 100%;">
    <img src="{{ current_mood.image | relative_url }}" alt="{{ current_mood.title }}" style="width: 100%; max-height: 600px; object-fit: cover; border-radius: 8px; display: block; margin-top: 10px;">
  </div>
  {% endif %}
</div>

[See full moodboard →]({{ '/moodboard/' | relative_url }}){: .btn .btn--light--outline}