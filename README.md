# Alessio Tonioni's Academic Website 🚀

This repository contains my personal academic website, featuring modern, AI-powered automation for research tracking.

## 🚀 Smart Features (Implemented by Antigravity)
This repository has been significantly refactored to include:

1.  **Automated Publication Updates**: A Python script ([update_publications.py](scripts/update_publications.py)) that you can run locally to scrape Google Scholar for your latest research.
2.  **AI News Generation**: Uses **Gemini 3 Flash** to generate catchy, informal news snippets for every new publication.
3.  **Transparency First**: AI-generated news is visually marked with a distinct purple badge on the website.
4.  **Local Control**: Run the script manually on your laptop whenever you want to check for updates.
5.  **Clean Repository**: Removed legacy theme junk and placeholder images for a premium, lightweight experience.

---

## 🛠️ Local Development & Updates

### 📦 Run the Routine Updates
The update scripts live in `scripts/` and run in this order:
1. `update_publications.py`: scrapes Google Scholar for new papers (patents and TD Commons disclosures are skipped) and writes `_publications/*.md` plus a Gemini-generated entry in `_data/news.yml`.
2. `process_publications_stats.py`: Semantic Scholar references, Gemini summaries/categories, embeddings and 2D map, written to `assets/data/publications_enhanced.json`. Results are cached per title in `_data/*_cache.json`, so only new papers trigger API calls. The stats describe what your papers cite (references), not citations received.
3. `update_projects.py`: proposes new GitHub repos as commented entries at the bottom of `_data/projects.yml`; uncomment the ones to feature.

Setup: `python -m venv .venv && .venv/bin/pip install -r requirements.txt`, then export `GEMINI_API_KEY` (and optionally `GITHUB_TOKEN`, e.g. `$(gh auth token)`, to avoid GitHub's anonymous rate limit).

The gitignored `scripts/local_update_run.sh` runs all three in sequence. Review the new publications and news before committing.

### 🖥️ Serve Locally
1.  Ensure you have Docker installed and running.
2.  Run the helper script: `./scripts/serve_local.sh`
3.  Visit the site at: `http://localhost:4000`

## ⚙️ CI/CD
The site is built and deployed via GitHub Actions. The publication automation requires a `GEMINI_API_KEY` to be set in the repository's secrets.
