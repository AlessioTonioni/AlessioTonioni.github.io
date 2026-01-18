import os
import json
import yaml
import requests
import time
import re
from pathlib import Path
from collections import Counter
from google import genai
import numpy as np
from sklearn.decomposition import PCA
import umap

# Configuration
PUBLICATIONS_DIR = "_publications"
PDF_CACHE_DIR = "_pdf_cache"
STATS_CACHE_FILE = "_data/stats_cache.json"
AI_CACHE_FILE = "_data/ai_results_cache.json"
OUTPUT_DATA_FILE = "assets/data/publications_enhanced.json"
S2_API_URL = "https://api.semanticscholar.org/graph/v1"
S2_API_KEY = os.environ.get("S2_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-3-flash-preview"
EMBEDDING_MODEL = "gemini-embedding-001"

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
        return None

    safe_title = re.sub(r'[^\w\s-]', '', title).strip().lower()
    safe_title = re.sub(r'[-\s]+', '-', safe_title)
    pdf_path = Path(PDF_CACHE_DIR) / f"{safe_title}.pdf"

    if pdf_path.exists():
        return str(pdf_path)

    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
            return str(pdf_path)
    except Exception as e:
        print(f"  ⚠ Failed to download PDF: {e}")
    
    return None

def s2_request(endpoint, params=None):
    """Helper for Semantic Scholar API requests with rate limiting."""
    headers = {}
    if S2_API_KEY:
        headers["x-api-key"] = S2_API_KEY
    
    url = f"{S2_API_URL}/{endpoint}"
    try:
        if not S2_API_KEY:
            time.sleep(1.1)
            
        response = requests.get(url, params=params, headers=headers, timeout=30)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print("  ⚠ Rate limited by Semantic Scholar. Waiting 60s...")
            time.sleep(60)
            return s2_request(endpoint, params)
        else:
            print(f"  ⚠ S2 API Error {response.status_code}")
    except Exception as e:
        print(f"  ⚠ S2 Request failed: {e}")
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
        if is_self_citation(ref.get("authors")):
            continue
            
        authors = ref.get("authors")
        if authors:
            for author in authors:
                auth_name = author.get("name")
                if auth_name and "tonioni" not in auth_name.lower():
                    author_counts[auth_name] += 1
        
        p_id = ref.get("paperId")
        if p_id:
            paper_counts[p_id] += 1
            paper_titles[p_id] = ref.get("title", "Unknown Title")
            
        year = ref.get("year")
        if year:
            year_counts[year] += 1
            
    top_author = author_counts.most_common(1)[0] if author_counts else ("None", 0)
    top_paper_id, top_paper_count = paper_counts.most_common(1)[0] if paper_counts else (None, 0)
    top_paper_title = paper_titles.get(top_paper_id, "None")
    influential_year = year_counts.most_common(1)[0] if year_counts else ("None", 0)
    
    return {
        "top_cited_author": {"name": top_author[0], "count": top_author[1]},
        "top_cited_paper": {"title": top_paper_title, "count": top_paper_count},
        "most_influential_year": {"year": influential_year[0], "count": influential_year[1]}
    }

def analyze_paper_with_gemini(client, title, pdf_path, abstract, max_retries=3):
    """Use Gemini to summarize and categorize a paper with retry logic."""
    prompt = f"""Analyze this research paper titled: "{title}"

Context: {abstract if abstract else "Abstract not available."}

Task:
1. Provide a one-sentence catchy summary (max 150 chars).
2. Assign ONE specific technical category (e.g., "3D Vision", "Depth Estimation", "Generative Models", "Vision-Language Models", etc.).

Return ONLY a JSON object:
{{
    "summary": "...",
    "category": "..."
}}"""
    
    for attempt in range(max_retries):
        try:
            if pdf_path and Path(pdf_path).exists():
                # Upload PDF to Gemini
                file_upload = client.files.upload(file=pdf_path)
                response = client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=[file_upload, prompt]
                )
            else:
                response = client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=prompt
                )
            
            text = response.text.strip()
            # Extract JSON
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(0))
        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                # Extract retry delay from error if available
                retry_match = re.search(r'retry in (\d+)', error_str)
                wait_time = int(retry_match.group(1)) + 5 if retry_match else 60
                print(f"  ⚠ Rate limited. Waiting {wait_time}s before retry {attempt + 1}/{max_retries}...")
                time.sleep(wait_time)
                continue
            else:
                print(f"  ⚠ Gemini analysis failed: {e}")
                break
    
    return {
        "summary": abstract[:150] + "..." if abstract else "No summary available.",
        "category": "Uncategorized"
    }

def get_embedding(client, text):
    """Fetch embedding for a given text."""
    try:
        result = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=text
        )
        # The API returns a list of embeddings
        return result.embeddings[0].values 
    except Exception as e:
        print(f"  ⚠ Embedding failed: {e}")
        return None

def normalize_categories(client, publications, max_retries=3):
    """Use Gemini to consolidate categories into a clean set with retry logic."""
    categories = list(set(
        pub.get('ai_results', {}).get('category', 'Uncategorized') 
        for pub in publications 
        if 'ai_results' in pub
    ))
    
    if len(categories) <= 8:
        return publications

    prompt = f"""I have {len(categories)} technical categories for research papers:
{categories}

Please group these into exactly 6-8 high-level, distinct technical domains.
Return a mapping from OLD category to NEW high-level domain.

Return ONLY a JSON object:
{{
    "old_name": "new_name",
    ...
}}"""
    
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
            text = response.text.strip()
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                mapping = json.loads(json_match.group(0))
                for pub in publications:
                    if 'ai_results' in pub:
                        old_cat = pub['ai_results']['category']
                        pub['ai_results']['category'] = mapping.get(old_cat, old_cat)
                return publications
        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                retry_match = re.search(r'retry in (\d+)', error_str)
                wait_time = int(retry_match.group(1)) + 5 if retry_match else 60
                print(f"  ⚠ Rate limited. Waiting {wait_time}s before retry {attempt + 1}/{max_retries}...")
                time.sleep(wait_time)
                continue
            else:
                print(f"  ⚠ Category normalization failed: {e}")
                break
    
    return publications

def project_embeddings(publications):
    """Project embeddings to 2D using UMAP and PCA."""
    embeds = []
    valid_pubs = []
    
    for pub in publications:
        if 'embedding' in pub and pub['embedding'] is not None:
            embeds.append(pub['embedding'])
            valid_pubs.append(pub)
    
    if len(embeds) < 2:
        print("  ⚠ Not enough embeddings for projection")
        return publications

    matrix = np.array(embeds)
    
    # PCA
    print("  Computing PCA projection...")
    pca = PCA(n_components=2)
    pca_results = pca.fit_transform(matrix)
    
    # UMAP
    print("  Computing UMAP projection...")
    n_neigh = min(len(embeds) - 1, 15)
    reducer = umap.UMAP(n_neighbors=max(2, n_neigh), min_dist=0.3, n_components=2, random_state=42)
    umap_results = reducer.fit_transform(matrix)
    
    # Store results
    for i, pub in enumerate(valid_pubs):
        pub['map_coords'] = {
            "pca": {"x": float(pca_results[i, 0]), "y": float(pca_results[i, 1])},
            "umap": {"x": float(umap_results[i, 0]), "y": float(umap_results[i, 1])}
        }
    
    return publications

def main():
    print("Step 1: Loading local publications...")
    local_pubs = load_local_publications()
    print(f"Found {len(local_pubs)} publications.\n")

    # Load caches
    s2_cache = {}
    if Path(STATS_CACHE_FILE).exists():
        with open(STATS_CACHE_FILE, 'r') as f:
            s2_cache = json.load(f)
    
    ai_cache = {}
    if Path(AI_CACHE_FILE).exists():
        with open(AI_CACHE_FILE, 'r') as f:
            ai_cache = json.load(f)
    
    # Initialize Gemini client
    gemini_client = None
    if GEMINI_API_KEY:
        gemini_client = genai.Client(api_key=GEMINI_API_KEY)
        print("✓ Gemini client initialized\n")
    else:
        print("⚠ GEMINI_API_KEY not set. Skipping AI enrichment.\n")
    
    all_references = []
    
    print("Step 2: Processing publications...\n")
    for i, pub in enumerate(local_pubs, 1):
        title = pub.get('title')
        print(f"[{i}/{len(local_pubs)}] {title[:60]}...")
        
        # Phase 1: Download PDFs
        url = pub.get('paperurl')
        if title and url:
            try:
                pub['pdf_path'] = download_pdf(title, url)
            except Exception:
                pass
        
        # Phase 2: S2 Matching & References
        if title not in s2_cache:
            s2_paper = find_s2_paper(title)
            if s2_paper:
                p_id = s2_paper['paperId']
                refs = fetch_paper_references(p_id)
                s2_cache[title] = {
                    "s2_id": p_id,
                    "references": refs,
                    "metadata": s2_paper
                }
            else:
                s2_cache[title] = None
        
        if s2_cache.get(title):
            all_references.extend(s2_cache[title]["references"])
            pub["s2_id"] = s2_cache[title]["s2_id"]
            pub["s2_metadata"] = s2_cache[title]["metadata"]
        
        # Phase 3: Gemini Analysis & Embeddings
        if gemini_client:
            if title not in ai_cache:
                print(f"  🤖 Analyzing with Gemini...")
                ai_result = analyze_paper_with_gemini(
                    gemini_client, 
                    title, 
                    pub.get('pdf_path'), 
                    pub.get('abstract')
                )
                embedding = get_embedding(gemini_client, ai_result['summary'])
                ai_cache[title] = {
                    "ai_results": ai_result,
                    "embedding": embedding
                }
                # Save cache immediately after each successful API call
                with open(AI_CACHE_FILE, 'w') as f:
                    json.dump(ai_cache, f, indent=2)
            
            if ai_cache.get(title):
                pub.update(ai_cache[title])
        
        print()

    # Category Normalization
    if gemini_client:
        print("\nStep 3: Normalizing categories...")
        local_pubs = normalize_categories(gemini_client, local_pubs)

    # Calculate Statistics
    print("\nStep 4: Calculating statistics...")
    stats = calculate_stats(all_references)
    
    # Project Embeddings
    print("\nStep 5: Projecting embeddings to 2D...")
    local_pubs = project_embeddings(local_pubs)

    # Save caches
    with open(STATS_CACHE_FILE, 'w') as f:
        json.dump(s2_cache, f, indent=2)
    with open(AI_CACHE_FILE, 'w') as f:
        json.dump(ai_cache, f, indent=2)

    # Prepare output (remove heavy embeddings)
    for pub in local_pubs:
        if 'embedding' in pub:
            del pub['embedding']

    output = {
        "publications": local_pubs,
        "stats": stats,
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open(OUTPUT_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"\n📊 Final Statistics:")
    print(f"  Most cited author: {stats['top_cited_author']['name']} ({stats['top_cited_author']['count']} citations)")
    print(f"  Most cited paper: {stats['top_cited_paper']['title'][:60]}... ({stats['top_cited_paper']['count']} citations)")
    print(f"  Most influential year: {stats['most_influential_year']['year']} ({stats['most_influential_year']['count']} papers)")
    print(f"\n✅ Phase 3 complete. Data saved to {OUTPUT_DATA_FILE}")

if __name__ == "__main__":
    main()
