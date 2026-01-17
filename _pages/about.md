---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes wave {
    0% { transform: rotate(0deg); }
    10% { transform: rotate(14deg); }
    20% { transform: rotate(-8deg); }
    30% { transform: rotate(14deg); }
    40% { transform: rotate(-4deg); }
    50% { transform: rotate(10deg); }
    60% { transform: rotate(0deg); }
    100% { transform: rotate(0deg); }
  }

  /* Research Tags */
  .interest-tag {
    display: inline-block;
    background: #f1f2f6;
    color: #2c3e50;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: 600;
    margin-right: 8px;
    margin-bottom: 8px;
    transition: all 0.2s ease;
  }
  .interest-tag:hover {
    background: #dfe4ea;
    transform: translateY(-2px);
  }

  /* Social Icons (Custom Main Content) */
  .social-icons-main {
    display: flex;
    gap: 20px;
    margin: 25px 0;
  }
  .social-icon-main {
    color: #b2bec3;
    font-size: 1.6em;
    transition: color 0.2s;
  }
  .social-icon-main:hover {
    color: #2c3e50;
  }

  /* Mood Feature Card */
  .mood-feature {
    display: flex;
    gap: 30px;
    background: #fff;
    border: 1px solid #f1f2f6;
    border-radius: 12px;
    padding: 25px;
    margin: 40px 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    align-items: flex-start;
  }
  
  .mood-image {
    flex: 0 0 300px;
    border-radius: 8px;
    overflow: hidden;
    cursor: zoom-in; /* Indicate clickable */
    position: relative;
  }
  
  .mood-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.5s ease;
  }
  
  .mood-image:hover img {
    transform: scale(1.05); /* Subtle zoom on hover */
  }

  .mood-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  @media (max-width: 768px) {
    .mood-feature { flex-direction: column; }
    .mood-image { flex: none; width: 100%; height: 250px; }
  }

  /* Lightbox Styles */
  .lightbox {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(30, 39, 46, 0.95); /* Darker Slate backdrop */
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
    cursor: zoom-out;
  }
  
  .lightbox.active {
    opacity: 1;
    pointer-events: all;
  }
  
  .lightbox img {
    max-width: 90%;
    max-height: 90vh;
    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
    border-radius: 4px;
    transform: scale(0.9);
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Bouncy pop */
  }
  
  .lightbox.active img {
    transform: scale(1);
  }

  .lightbox-close {
    position: absolute;
    top: 30px;
    right: 40px;
    color: #fff;
    font-size: 40px;
    cursor: pointer;
    opacity: 0.7;
    transition: opacity 0.2s;
  }
  
  .lightbox-close:hover {
    opacity: 1;
  }

  /* News Modernization */
  .news-timeline {
    position: relative;
    border-left: 2px solid #dfe6e9;
    padding-left: 30px;
    margin-top: 30px;
  }
  .news-card {
    position: relative;
    background: #fff;
    border-radius: 8px;
    padding: 15px 20px;
    margin-bottom: 25px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    border: 1px solid #f1f2f6;
    transition: transform 0.2s;
  }
  .news-card:hover {
    transform: translateX(5px);
    border-left: 3px solid #1abc9c;
  }
  .news-dot {
    position: absolute;
    left: -36px;
    top: 20px;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #1abc9c;
    border: 2px solid #fff;
    box-shadow: 0 0 0 2px #dfe6e9;
  }
</style>

<div class="hero-content" style="animation: fadeIn 0.8s ease-out;">
  <h1 style="font-size: 2.8em; margin-bottom: 0.2em; font-weight: 800; letter-spacing: -1px;">Hi, I'm Alessio <span style="display:inline-block; animation: wave 2s infinite">👋</span></h1>
  
  <div style="margin: 20px 0;">
    <span class="interest-tag">🤖 Generative AI</span>
    <span class="interest-tag">🕶️ Egocentric Vision</span>
    <span class="interest-tag">🖼️ Image Understanding</span>
    <span class="interest-tag">🎬 Video Understanding</span>
  </div>

  <div style="font-size: 1.15em; line-height: 1.6; color: #2d3436; max-width: 100%;">
    <p>
      I am an <strong>AI Researcher</strong> at <strong>Google XR Zurich</strong> in <a href="https://federicotombari.github.io/" style="color: #2c3e50; font-weight: 600; text-decoration: underline; text-decoration-color: #1abc9c;">Federico Tombari</a>'s team. I lead my own applied research team focused on AI technologies for the current and next generation of XR devices. We work on the whole stack ranging from the integration of AI technologies to improving Gemini for egocentric assistant use cases.
    </p>

    <p>
      I earned my Ph.D. in Computer Science and Engineering from the <strong>University of Bologna</strong> in 2019 at the <a href="https://www.vision.deis.unibo.it/">Computer Vision Lab</a>, advised by Professor <a href="https://scholar.google.ch/citations?user=xZVTzyAAAAAJ&hl=de">Luigi Di Stefano</a>.
    </p>

    <p>
      My research journey began with deep learning for retail environments and depth estimation for autonomous driving. Since then, it has evolved through several different topics, ranging from implementing some of the visual translation stack powering Google Lens and Google translate to different image understanding tasks without forgetting some of my early 3D reconstruction and generation works. My current focus is on <strong>multimodal video/image understanding and generation</strong> using LLMs and Diffusion models.
    </p>

    <p>
      I'm always excited to discuss new ideas or explore emerging topics. If you find any of our work interesting, please don't hesitate to reach out!
    </p>
  </div>

  <div class="social-icons-main">
    <a href="mailto:alessio.tonioni.91@gmail.com" class="social-icon-main" title="Email"><i class="fas fa-envelope"></i></a>
    <a href="https://www.linkedin.com/in/alessio-tonioni-16261668" class="social-icon-main" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
    <a href="https://github.com/AlessioTonioni" class="social-icon-main" title="GitHub"><i class="fab fa-github"></i></a>
    <a href="https://scholar.google.it/citations?user=ry_BLFUAAAAJ&hl=en" class="social-icon-main" title="Google Scholar"><i class="fas fa-graduation-cap"></i></a>
  </div>
</div>

<!-- Mood Spotlight (Wide Layout) -->
{% assign current_mood = site.data.moods | first %}
<div class="mood-feature">
  {% if current_mood.image %}
  <div class="mood-image" onclick="openLightbox('{{ current_mood.image | relative_url }}')">
    <img src="{{ current_mood.image | relative_url }}" alt="{{ current_mood.title }}">
  </div>
  {% endif %}
  
  <div class="mood-content">
    <h4 style="margin: 0 0 10px 0; color: #b2bec3; text-transform: uppercase; font-size: 0.8em; letter-spacing: 1.5px;">Current Mood</h4>
    <h2 style="margin: 0 0 10px 0; font-size: 1.5em; color: #2d3436;">{{ current_mood.title }}</h2>
    <p style="font-size: 1.05em; color: #636e72; font-style: italic; margin-bottom: 20px;">
      "{{ current_mood.description }}"
    </p>

    <div style="display: flex; gap: 15px; align-items: center;">
       {% if current_mood.youtube_id %}
        <a href="https://www.youtube.com/watch?v={{ current_mood.youtube_id }}" target="_blank" class="btn btn--danger" style="margin: 0; padding: 8px 16px; border-radius: 30px;">
          <i class="fas fa-play" style="margin-right: 5px;"></i> Play Soundtrack
        </a>
       {% endif %}
       <a href="{{ '/moodboard/' | relative_url }}" style="color: #636e72; font-size: 0.9em; text-decoration: none; border-bottom: 1px dashed #b2bec3;">View History →</a>
    </div>
  </div>
</div>

---

<h2 style="margin-top: 40px; border-bottom: 2px solid #f1f2f6; padding-bottom: 10px;">Latest News</h2>

<div class="news-timeline">
  {% assign latest_news = site.data.news | sort: "date" | reverse | slice: 0, 5 %}
  {% for item in latest_news %}
    <div class="news-card">
      <div class="news-dot"></div>
      <span style="display: block; font-size: 0.8em; color: #b2bec3; margin-bottom: 5px; font-weight: 600;">{{ item.date | date: "%B %Y" }}</span>
      <div style="color: #2d3436; line-height: 1.5;">
        {{ item.content | markdownify }}
      </div>
    </div>
  {% endfor %}
</div>

<div style="text-align: center; margin-top: 30px;">
  <a href="{{ '/news/' | relative_url }}" class="btn btn--light--outline">View All News</a>
</div>

<!-- Lightbox Markup -->
<div id="mood-lightbox" class="lightbox" onclick="closeLightbox()">
  <span class="lightbox-close">&times;</span>
  <img id="lightbox-img" src="" alt="Mood Fullscreen">
</div>

<script>
function openLightbox(src) {
  const lightbox = document.getElementById('mood-lightbox');
  const img = document.getElementById('lightbox-img');
  img.src = src;
  lightbox.classList.add('active');
  document.body.style.overflow = 'hidden'; // Prevent scrolling background
}

function closeLightbox() {
  const lightbox = document.getElementById('mood-lightbox');
  lightbox.classList.remove('active');
  document.body.style.overflow = ''; // Restore scrolling
}

// Close on Escape key
document.addEventListener('keydown', function(event) {
  if (event.key === "Escape") {
    closeLightbox();
  }
});
</script>