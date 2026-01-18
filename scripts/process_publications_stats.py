import os
import json
import yaml
import requests
import time
import re
from pathlib import Path

# Configuration
PUBLICATIONS_DIR = "_publications"
PDF_CACHE_DIR = "_pdf_cache"
OUTPUT_DATA_FILE = "assets/data/publications_enhanced.json"

# Ensure directories exist
Path(PDF_CACHE_DIR).mkdir(exist_ok=True)
Path("assets/data").mkdir(parents=True, exist_ok=True)

def load_local_publications():
    """Load publication data from local markdown files."""
    publications = []
    pub_path = Path(PUBLICATIONS_DIR)
    if not pub_path.exists():
        return publications

    for file in pub_path.glob("*.md"):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            parts = content.split('---')
            if len(parts) >= 3:
                try:
                    metadata = yaml.safe_load(parts[1])
                    metadata['local_file'] = str(file)
                    # Extract abstract if available in markdown
                    abstract_match = re.search(r'## Abstract\n\n(.*?)(\n\n|\||\Z)', content, re.DOTALL)
                    if abstract_match:
                        metadata['abstract'] = abstract_match.group(1).strip()
                    publications.append(metadata)
                except Exception as e:
                    print(f"Error parsing {file}: {e}")
    return publications

def download_pdf(title, url):
    """Download PDF to cache if not already present."""
    if not url:
        return None
    
    # Arxiv conversion
    if isinstance(url, str) and 'arxiv.org/abs/' in url:
        url = url.replace('arxiv.org/abs/', 'arxiv.org/pdf/') + '.pdf'

    if isinstance(url, str) and 'arxiv.org/pdf/' in url and not url.endswith('.pdf'):
        url = url + '.pdf'
    
    if not isinstance(url, str) or not url.endswith('.pdf'):
        print(f"Invalid URL for {title}: {url}")
        return None

    safe_title = re.sub(r'[^\w\s-]', '', title).strip().lower()
    safe_title = re.sub(r'[-\s]+', '-', safe_title)
    pdf_path = Path(PDF_CACHE_DIR) / f"{safe_title}.pdf"

    if pdf_path.exists():
        return str(pdf_path)

    try:
        print(f"Downloading PDF for: {title} with title")
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
            return str(pdf_path)
    except Exception as e:
        print(f"Failed to download PDF from {url} to file {pdf_path}: {e}")
    
    return None

def main():
    print("Step 1: Loading local publications...")
    local_pubs = load_local_publications()
    print(f"Found {len(local_pubs)} publications.")

    # Phase 1: Download PDFs
    for pub in local_pubs:
        title = pub.get('title')
        url = pub.get('paperurl')
        if title and url:
            try:
                pub['pdf_path'] = download_pdf(title, url)
            except Exception as e:
                continue

    # Initial save of what we have
    with open(OUTPUT_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(local_pubs, f, indent=2, default=str)
    
    print(f"Phase 1 complete. Data saved to {OUTPUT_DATA_FILE}")

if __name__ == "__main__":
    main()
