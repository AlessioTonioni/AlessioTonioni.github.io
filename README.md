# Alessio Tonioni's Academic Website 🚀

This repository contains my personal academic website, featuring modern, AI-powered automation for research tracking.

## 🚀 Smart Features (Implemented by Antigravity)
This repository has been significantly refactored to include:

1.  **Automated Publication Updates**: A Python script ([update_publications.py](scripts/update_publications.py)) automatically scrapes Google Scholar for new research.
2.  **AI News Generation**: Uses **Gemini 3 Flash** to generate catchy, informal news snippets for every new publication.
3.  **Transparency First**: AI-generated news is visually marked with a distinct purple badge on the website.
4.  **Weekly Schedule**: Powered by GitHub Actions to run every Sunday at midnight.
5.  **Secure Notifications**: Automatically opens a **GitHub Issue** with a summary of changes whenever an update is implemented or if an error occurs.
6.  **Clean Repository**: Removed legacy theme junk and placeholder images for a premium, lightweight experience.

---

## 🛠️ Local Development

1.  Clone the repository.
2.  Make sure you have Ruby, Bundler, and Nodejs installed.
3.  Run `bundle install` to install dependencies.
4.  Run `bundle exec jekyll liveserve` to serve it from `localhost:4000`.

## ⚙️ CI/CD
The site is built and deployed via GitHub Actions. The publication automation requires a `GEMINI_API_KEY` to be set in the repository's secrets.
