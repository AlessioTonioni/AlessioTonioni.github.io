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

  /* Unified Spotlight Features */
  .features-container {
    display: flex;
    flex-direction: column;
    gap: 25px;
    margin: 40px 0;
  }

  .mood-feature, .project-feature {
    display: flex;
    gap: 35px;
    background: #fff;
    border: 1px solid #f0f3f6;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    text-decoration: none !important;
    color: inherit !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    align-items: center;
  }

  .mood-feature:hover, .project-feature:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    border-color: #1abc9c;
  }

  /* Visual Elements (Left Side) */
  .mood-image, .project-visual {
    flex: 0 0 240px;
    height: 150px;
    border-radius: 10px;
    overflow: hidden;
    position: relative;
    background: #f8fafc;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .mood-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.5s ease;
  }

  .mood-feature:hover .mood-image img {
    transform: scale(1.05);
  }

  .project-visual {
    background: linear-gradient(135deg, #f1f2f6 0%, #dfe4ea 100%);
    color: #1abc9c;
    font-size: 3.5em;
    transition: all 0.3s ease;
  }

  .project-feature:hover .project-visual {
    background: linear-gradient(135deg, #e6f7f4 0%, #1abc9c15 100%);
    transform: rotate(-3deg) scale(1.05);
  }

  /* Content Elements (Right Side) */
  .mood-content, .project-content {
    flex: 1;
    min-width: 0;
  }

  .feature-label {
    margin: 0 0 8px 0;
    color: #b2bec3;
    text-transform: uppercase;
    font-size: 0.75em;
    font-weight: 700;
    letter-spacing: 1.2px;
  }

  .feature-title {
    margin: 0 0 8px 0;
    font-size: 1.4em;
    color: #2d3436;
    font-weight: 800;
  }

  .feature-desc {
    font-size: 0.95em;
    color: #636e72;
    line-height: 1.5;
    margin-bottom: 12px;
  }

  .feature-more {
    color: #1abc9c;
    font-size: 0.9em;
    font-weight: 600;
    text-decoration: none;
    border-bottom: 2px solid transparent;
    transition: border-color 0.2s;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }

  .mood-feature:hover .feature-more, .project-feature:hover .feature-more {
    border-bottom-color: #1abc9c;
  }

  @media (max-width: 768px) {
    .mood-feature, .project-feature {
      flex-direction: column;
      align-items: flex-start;
      gap: 20px;
      padding: 20px;
    }
    .mood-image, .project-visual {
      flex: none;
      width: 100%;
      height: 200px;
    }
  }

  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
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
    border-left: 3px solid transparent; 
    transition: all 0.2s ease;
  }
  .news-card:hover {
    transform: translateX(6px);
    border-left-color: #1abc9c;
    box-shadow: 0 6px 15px rgba(0,0,0,0.06);
  }
  .news-card:hover .news-dot {
    transform: translateX(-6px);
  }
  .news-dot {
    position: absolute;
    left: -40px;
    top: 20px;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #1abc9c;
    border: 2px solid #fff;
    box-shadow: 0 0 0 2px #dfe6e9;
    transition: transform 0.2s ease;
    z-index: 1;
  }
</style>

<div class="hero-content" style="animation: fadeIn 0.8s ease-out;">
  <h1 style="font-size: 2.8em; margin-bottom: 0.2em; font-weight: 800; letter-spacing: -1px;">Hi, I'm Alessio</h1>
  
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
    <a href="{{ '/files/CV.pdf' | relative_url }}" class="social-icon-main" title="CV"><i class="fas fa-file-pdf"></i></a>
    <a href="https://www.linkedin.com/in/alessio-tonioni-16261668" class="social-icon-main" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
    <a href="https://github.com/AlessioTonioni" class="social-icon-main" title="GitHub"><i class="fab fa-github"></i></a>
    <a href="https://scholar.google.it/citations?user=ry_BLFUAAAAJ&hl=en" class="social-icon-main" title="Google Scholar"><i class="fas fa-graduation-cap"></i></a>
  </div>
</div>

<!-- Features Container: Mood Spotlight & Project Spotlight -->
<div class="features-container">
  {% assign current_mood = site.data.moods | first %}
  <div class="mood-feature" onclick="openLightbox('{{ current_mood.image | relative_url }}')">
    {% if current_mood.image %}
    <div class="mood-image">
      <img src="{{ current_mood.image | relative_url }}" alt="{{ current_mood.title }}">
    </div>
    {% endif %}
    
    <div class="mood-content">
      <h4 class="feature-label">Current Mood</h4>
      <div style="display: flex; align-items: center; margin-bottom: 8px;">
        <h3 class="feature-title" style="margin-bottom: 0;">{{ current_mood.title }}</h3>
        {% if current_mood.youtube_id %}
        <a href="https://www.youtube.com/watch?v={{ current_mood.youtube_id }}" target="_blank" title="Play Soundtrack" style="margin-left: 10px; color: #e17055; font-size: 1.1em; transition: transform 0.2s; display: inline-block;">
          <i class="fas fa-music"></i>
        </a>
        {% endif %}
      </div>
      <p class="feature-desc" style="font-style: italic;">
        "{{ current_mood.description }}"
      </p>
      <span class="feature-more">Explore Moodboard →</span>
    </div>
  </div>

  <!-- Random Side Project Spotlight -->
  <a id="random-project-link" href="{{ '/projects/' | relative_url }}" class="project-feature">
    <div class="project-visual">
       <i id="random-project-icon" class="fas fa-code"></i>
    </div>
    <div class="project-content">
      <h4 class="feature-label">Random Side Project</h4>
      <h3 id="random-project-title" class="feature-title">Loading...</h3>
      <p id="random-project-desc" class="feature-desc line-clamp-2">
        Discovering a cool side project...
      </p>
      <span class="feature-more">View Projects →</span>
    </div>
  </a>
</div>

<script>
  const projectsData = {{ site.data.projects | jsonify }} || [];

  document.addEventListener("DOMContentLoaded", function() {
    if (projectsData.length > 0) {
      const randomIndex = Math.floor(Math.random() * projectsData.length);
      const proj = projectsData[randomIndex];
      
      document.getElementById("random-project-title").innerText = proj.title;
      document.getElementById("random-project-desc").innerText = proj.description;
      document.getElementById("random-project-icon").className = (proj.icon || "fas fa-code");
    }
  });
</script>

---

<h2 style="margin-top: 40px; border-bottom: 2px solid #f1f2f6; padding-bottom: 10px;">Latest News</h2>

<div class="news-timeline">
  {% assign latest_news = site.data.news | sort: "date" | reverse | slice: 0, 5 %}
  {% for item in latest_news %}
    <div class="news-card">
      <div class="news-dot"></div>
      <div style="display: flex; align-items: center; margin-bottom: 5px;">
        <span style="font-size: 0.8em; color: #b2bec3; font-weight: 600;">{{ item.date | date: "%B %Y" }}</span>
        {% if item.ai_generated %}
          <span class="ai-badge"><i class="fas fa-robot"></i> AI Generated</span>
        {% endif %}
      </div>
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