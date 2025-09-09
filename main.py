#!/usr/bin/env python3
"""
Simple file reader for temp-log-data GitHub repository.
GitHub URL: https://github.com/CarbonSiliconAI/temp-log-data
"""

import requests

# Configuration - Change these variables as needed
REPO_OWNER = "CarbonSiliconAI"
REPO_NAME = "temp-log-data"
SLUG = "ethereum-above-4400-on-september-8"
FILES = {
    "log": "app.log",
    "transactions": "transaction_list.json",
    "summary": "transaction_summary.json"
}

def get_file_content(slug: str, filename: str) -> str:
    """Get file content from GitHub repository."""
    url = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/main/{slug}/{filename}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {filename}: {e}")
        return ""

def main():
    """Demo: fetch and display file contents."""
    print(f"Reading files from: {REPO_OWNER}/{REPO_NAME}/{SLUG}")
    print("=" * 50)
    
    for file_type, filename in FILES.items():
        print(f"\n--- {file_type.upper()}: {filename} ---")
        content = get_file_content(SLUG, filename)
        
        if content:
            # Show first few lines for preview
            lines = content.split('\n')[:5]
            for i, line in enumerate(lines, 1):
                if line.strip():
                    print(f"{i}: {line}")
            
            if len(content.split('\n')) > 5:
                total_lines = len(content.split('\n'))
                print(f"... ({total_lines} total lines)")
        else:
            print("Failed to fetch content")

if __name__ == "__main__":
    main()