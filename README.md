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

### 📦 Run Publication Updates
To check for new papers and generate news:
1.  Ensure you have your `GEMINI_API_KEY` exported in your terminal: `export GEMINI_API_KEY=your_key_here`
2.  Install requirements: `pip install scholarly pyyaml google-genai`
3.  Run the script: `python scripts/update_publications.py`
4.  Review the new markdown files in `_publications/` and the updates in `_data/news.yml`.
5.  Commit and push: `git add . && git commit -m "Update publications" && git push`

### 🖥️ Serve Locally
1.  Ensure you have Docker installed and running.
2.  Run the helper script: `./scripts/serve_local.sh`
3.  Visit the site at: `http://localhost:4000`

## ⚙️ CI/CD
The site is built and deployed via GitHub Actions. The publication automation requires a `GEMINI_API_KEY` to be set in the repository's secrets.
