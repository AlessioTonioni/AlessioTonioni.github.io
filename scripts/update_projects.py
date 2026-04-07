#!/usr/bin/env python3

import urllib.request
import json
import yaml
import os

GITHUB_USER = "AlessioTonioni"
API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100&type=owner"
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', '_data', 'projects.yml')

import ssl
try:
    from google import genai
    from dotenv import load_dotenv
    load_dotenv()
    have_gemini = True
except ImportError:
    have_gemini = False

def get_repos():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    req = urllib.request.Request(API_URL, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return []

def update_projects_file():
    repos = get_repos()
    
    if not repos:
        print("No repos found or error occurred.")
        return

    # Load existing projects to keep existing manual edits (like icons and custom tags)
    existing_projects = []
    ignored_urls = set()
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            content = f.read()
            import re
            # Find URLs that are commented out
            for match in re.finditer(r'#\s*url:\s*"([^"]+)"', content):
                ignored_urls.add(match.group(1))
            
            # Reset file pointer to read as yaml
            f.seek(0)
            existing_projects = yaml.safe_load(f) or []

    # Map existing over URL
    existing_map = {p.get('url'): p for p in existing_projects if p.get('url')}

    # Default icon mapping based on language or tags
    def guess_icon_default(repo):
        lang = (repo.get('language') or '').lower()
        if 'python' in lang or 'jupyter' in lang:
            return 'fab fa-python'
        if 'typescript' in lang or 'javascript' in lang:
            return 'fab fa-js'
        if 'html' in lang:
            return 'fab fa-html5'
        return 'fas fa-code'

    def guess_icon(repo):
        if have_gemini and os.environ.get("GEMINI_API_KEY"):
            try:
                client = genai.Client()
                desc = repo.get('description') or repo.get('name') or ''
                prompt = f"Return exactly one FontAwesome v5 class string (like 'fas fa-code' or 'fas fa-robot') that best represents a github repository with this description: '{desc}'. Return ONLY the class string, nothing else. No quotes."
                response = client.models.generate_content(
                    model='gemini-3-flash-preview',
                    contents=prompt,
                )
                icon = response.text.strip().replace('`', '').strip()
                if icon.startswith('fas fa-') or icon.startswith('fab fa-') or icon.startswith('fa-'):
                    return icon
            except Exception as e:
                print(f"  [Gemini icon generation failed: {e}]")
        return guess_icon_default(repo)

    new_projects = []
    
    print("Fetching active repositories...")
    
    for repo in repos:
        # Ignore forks and empty repos
        if repo.get('fork') or repo.get('private'):
            continue
            
        repo_url = repo.get('html_url')
        
        # If the user already has this project in projects.yml, we keep their manual values, 
        # but maybe update description if it's missing.
        if repo_url in existing_map:
            p = existing_map[repo_url]
            new_projects.append(p)
            print(f"Keeping existing project: {p.get('title')}")
            continue
        pass
        
    print("\n--- Available Repositories ---")
    
    with open(DATA_FILE, 'a') as f:
        f.write("\n# --- NEW REPOSITORIES FETCHED BY SCRIPT ---\n")
        f.write("# Uncomment any of the following to advertise them on your website:\n\n")
        for repo in repos:
            repo_url = repo.get('html_url')
            if repo.get('fork') or repo.get('private') or repo_url in existing_map or repo_url in ignored_urls:
                continue
            
            print(f"Proposing: {repo.get('name')}")
            
            desc = repo.get('description') or repo.get('name') or ''
            # Escape quotes in description to be safe
            desc = desc.replace('"', '\\"')
            
            f.write(f"# - title: \"{repo.get('name')}\"\n")
            f.write(f"#   description: \"{desc}\"\n")
            f.write(f"#   url: \"{repo_url}\"\n")
            f.write(f"#   tags: [\"{repo.get('language') or 'Misc'}\"]\n")
            f.write(f"#   icon: \"{guess_icon(repo)}\"\n\n")
            
    print(f"\nSuccessfully proposed new projects. Please check {DATA_FILE} and uncomment to finalize.")

if __name__ == "__main__":
    update_projects_file()
