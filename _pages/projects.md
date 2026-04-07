---
permalink: /projects/
title: "Side Projects"
author_profile: true
---

<style>
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 30px;
  }
  
  .project-card {
    background: #fff;
    border: 1px solid #f1f2f6;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
    color: inherit;
    position: relative;
    overflow: hidden;
  }
  
  .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.08);
    border-color: #1abc9c;
  }
  
  .project-icon {
    font-size: 2.5em;
    color: #1abc9c;
    margin-bottom: 20px;
    transition: transform 0.3s ease;
  }
  
  .project-card:hover .project-icon {
    transform: scale(1.1);
  }
  
  .project-title {
    font-size: 1.4em;
    font-weight: 700;
    color: #2d3436;
    margin: 0 0 10px 0;
  }
  
  .project-description {
    font-size: 1em;
    color: #636e72;
    line-height: 1.5;
    margin: 0 0 20px 0;
    flex-grow: 1;
  }
  
  .project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: auto;
  }
  
  .project-tag {
    background: #f1f2f6;
    color: #2c3e50;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.8em;
    font-weight: 600;
  }
  
  .github-corner {
    position: absolute;
    top: 15px;
    right: 15px;
    color: #b2bec3;
    font-size: 1.2em;
    transition: color 0.3s;
  }
  
  .project-card:hover .github-corner {
    color: #2c3e50;
  }
</style>

<div style="animation: fadeIn 0.8s ease-out;">
  <p style="font-size: 1.15em; line-height: 1.6; color: #2d3436;">
    A collection of my "vibecoding" side projects—small, experimental, or weekend creations driven by curiosity. These are mostly hosted on my GitHub.
  </p>

  <div class="projects-grid">
    {% for project in site.data.projects %}
      <a href="{{ project.url }}" class="project-card" target="_blank" rel="noopener noreferrer">
        <i class="{{ project.icon | default: 'fas fa-code' }} project-icon"></i>
        <i class="fab fa-github github-corner"></i>
        
        <h3 class="project-title">{{ project.title }}</h3>
        <p class="project-description">{{ project.description }}</p>
        
        <div class="project-tags">
          {% for tag in project.tags %}
            <span class="project-tag">{{ tag }}</span>
          {% endfor %}
        </div>
      </a>
    {% endfor %}
  </div>
</div>
