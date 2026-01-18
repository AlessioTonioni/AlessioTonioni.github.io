import os
import json
import yaml
import requests
import time
import re
from pathlib import Path
from collections import Counter

# Configuration
PUBLICATIONS_DIR = "_publications"
PDF_CACHE_DIR = "_pdf_cache"
STATS_CACHE_FILE = "_data/stats_cache.json"
OUTPUT_DATA_FILE = "assets/data/publications_enhanced.json"
S2_API_URL = "https://api.semanticscholar.org/graph/v1"
S2_API_KEY = os.environ.get("S2_API_KEY")  # Optional but recommended

# Ensure directories exist
Path(PDF_CACHE_DIR).mkdir(exist_ok=True)
Path("assets/data").mkdir(parents=True, exist_ok=True)
Path("_data").mkdir(exist_ok=True)

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

def s2_request(endpoint, params=None):
    """Helper for Semantic Scholar API requests with rate limiting."""
    headers = {}
    if S2_API_KEY:
        headers["x-api-key"] = S2_API_KEY
    
    url = f"{S2_API_URL}/{endpoint}"
    try:
        # Respect rate limits (1 req/sec without key, 100 req/sec with key)
        if not S2_API_KEY:
            time.sleep(1.1)
            
        response = requests.get(url, params=params, headers=headers, timeout=30)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print("Rate limited by Semantic Scholar. Waiting 60s...")
            time.sleep(60)
            return s2_request(endpoint, params)
        else:
            print(f"S2 API Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"S2 Request failed: {e}")
    return None

def find_s2_paper(title):
    """Match a publication title to a Semantic Scholar ID."""
    params = {
        "query": title, 
        "limit": 1, 
        "fields": "paperId,title,authors,year,referenceCount,citationCount"
    }
    data = s2_request("paper/search", params)
    if data and data.get("data"):
        return data["data"][0]
    return None

def fetch_paper_references(paper_id):
    """Fetch all references for a given paper ID."""
    params = {"fields": "paperId,title,authors,year,venue", "limit": 1000}
    data = s2_request(f"paper/{paper_id}/references", params)
    if data and data.get("data"):
        return [ref.get("citedPaper") for ref in data["data"] if ref.get("citedPaper")]
    return []

def is_self_citation(authors_list):
    """Check if 'Tonioni' is among the authors."""
    if not authors_list:
        return False
    for author in authors_list:
        name = author.get("name", "").lower() if isinstance(author, dict) else str(author).lower()
        if "tonioni" in name:
            return True
    return False

def calculate_stats(all_references):
    """Calculate citation statistics from aggregated references."""
    author_counts = Counter()
    paper_counts = Counter()
    year_counts = Counter()
    paper_titles = {}
    
    for ref in all_references:
        # Skip self-citations
        if is_self_citation(ref.get("authors")):
            continue
            
        # Track authors
        authors = ref.get("authors")
        if authors:
            for author in authors:
                auth_name = author.get("name")
                if auth_name and "tonioni" not in auth_name.lower():
                    author_counts[auth_name] += 1
        
        # Track papers
        p_id = ref.get("paperId")
        if p_id:
            paper_counts[p_id] += 1
            paper_titles[p_id] = ref.get("title", "Unknown Title")
            
        # Track years
        year = ref.get("year")
        if year:
            year_counts[year] += 1
            
    # Get top items
    top_author = author_counts.most_common(1)[0] if author_counts else ("None", 0)
    top_paper_id, top_paper_count = paper_counts.most_common(1)[0] if paper_counts else (None, 0)
    top_paper_title = paper_titles.get(top_paper_id, "None")
    influential_year = year_counts.most_common(1)[0] if year_counts else ("None", 0)
    
    return {
        "top_cited_author": {"name": top_author[0], "count": top_author[1]},
        "top_cited_paper": {"title": top_paper_title, "count": top_paper_count},
        "most_influential_year": {"year": influential_year[0], "count": influential_year[1]}
    }

def main():
    print("Step 1: Loading local publications...")
    local_pubs = load_local_publications()
    print(f"Found {len(local_pubs)} publications.")

    # Load cache if exists
    s2_cache = {}
    if Path(STATS_CACHE_FILE).exists():
        with open(STATS_CACHE_FILE, 'r') as f:
            s2_cache = json.load(f)
    
    all_references = []
    
    print("\nStep 2: Processing publications...")
    for i, pub in enumerate(local_pubs, 1):
        title = pub.get('title')
        print(f"[{i}/{len(local_pubs)}] {title[:60]}...")
        
        # Phase 1: Download PDFs
        url = pub.get('paperurl')
        if title and url:
            try:
                pub['pdf_path'] = download_pdf(title, url)
            except Exception as e:
                continue
        
        # Phase 2: S2 Matching & References
        if title not in s2_cache:
            s2_paper = find_s2_paper(title)
            if s2_paper:
                p_id = s2_paper['paperId']
                print(f"  ✓ Found S2 ID: {p_id}. Fetching references...")
                refs = fetch_paper_references(p_id)
                s2_cache[title] = {
                    "s2_id": p_id,
                    "references": refs,
                    "metadata": s2_paper
                }
                print(f"  ✓ Found {len(refs)} references")
            else:
                print(f"  ✗ No S2 match found")
                s2_cache[title] = None
        else:
            print(f"  ✓ Using cached S2 data")
        
        if s2_cache.get(title):
            all_references.extend(s2_cache[title]["references"])
            pub["s2_id"] = s2_cache[title]["s2_id"]
            pub["s2_metadata"] = s2_cache[title]["metadata"]

    # Calculate statistics
    print("\nStep 3: Calculating statistics...")
    stats = calculate_stats(all_references)
    print(f"\n📊 Statistics:")
    print(f"  Most cited author: {stats['top_cited_author']['name']} ({stats['top_cited_author']['count']} citations)")
    print(f"  Most cited paper: {stats['top_cited_paper']['title'][:60]}... ({stats['top_cited_paper']['count']} citations)")
    print(f"  Most influential year: {stats['most_influential_year']['year']} ({stats['most_influential_year']['count']} papers)")

    # Save cache
    with open(STATS_CACHE_FILE, 'w') as f:
        json.dump(s2_cache, f, indent=2)

    # Save output
    output = {
        "publications": local_pubs,
        "stats": stats,
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open(OUTPUT_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"\n✅ Phase 2 complete. Data saved to {OUTPUT_DATA_FILE}")

if __name__ == "__main__":
    main()
