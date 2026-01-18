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

<script src="https://cdn.plot.ly/plotly-2.27.0.min.js" charset="utf-8"></script>

<style>
.stats-container {
    display: flex;
    justify-content: space-around;
    gap: 20px;
    margin: 30px 0 40px 0;
    flex-wrap: wrap;
}
.stat-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    flex: 1;
    min-width: 250px;
    text-align: center;
    color: white;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}
.stat-card:nth-child(2) {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}
.stat-card:nth-child(3) {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}
.stat-value {
    font-size: 1.3em;
    font-weight: bold;
    margin: 10px 0;
    line-height: 1.4;
}
.stat-label {
    font-size: 0.85em;
    text-transform: uppercase;
    letter-spacing: 1px;
    opacity: 0.9;
}
.map-container {
    background: white;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 50px;
    border: 1px solid #f0f0f0;
}
.map-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
    flex-wrap: wrap;
    gap: 15px;
}
.map-header h2 {
    margin: 0;
    color: #2c3e50;
    font-size: 1.6em;
}
.map-toggle {
    display: flex;
    gap: 10px;
}
.toggle-btn {
    padding: 8px 18px;
    border: 2px solid #ddd;
    background: white;
    cursor: pointer;
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: 500;
    transition: all 0.3s ease;
}
.toggle-btn:hover {
    border-color: #667eea;
    color: #667eea;
}
.toggle-btn.active {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-color: #667eea;
}
.map-description {
    color: #666;
    font-size: 0.9em;
    margin-bottom: 20px;
    line-height: 1.6;
}
</style>

<div class="stats-container" id="pub-stats">
    <div class="stat-card">
        <div class="stat-label">📚 Top 5 Cited Authors (by me)</div>
        <div class="stat-value" id="stat-authors" style="font-size: 0.95em; text-align: left;">Loading...</div>
    </div>
    <div class="stat-card">
        <div class="stat-label">📄 Top 5 Cited Papers (by me)</div>
        <div class="stat-value" id="stat-papers" style="font-size: 0.85em; text-align: left;">Loading...</div>
    </div>
    <div class="stat-card">
        <div class="stat-label">⏳ Most Influential Year</div>
        <div class="stat-value" id="stat-year">Loading...</div>
    </div>
</div>

<div class="map-container">
    <div class="map-header">
        <h2>🗺️ Paper Conceptual Map</h2>
        <div class="map-toggle">
            <button class="toggle-btn active" onclick="updateMap('umap')">UMAP</button>
            <button class="toggle-btn" onclick="updateMap('pca')">PCA</button>
        </div>
    </div>
    <p class="map-description">
        My publications plotted in 2D based on semantic embeddings of their summaries. 
        Each point represents a paper, colored by research area. 
        Hover to see summaries, click to jump to the paper below.
    </p>
    <div id="pub-map" style="height: 500px; width: 100%;"></div>
</div>

<script src="/assets/js/publications_viz.js"></script>

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


