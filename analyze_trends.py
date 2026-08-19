import json
from collections import Counter
import re

def analyze_headlines():
    file_path = "data/headlines.json"
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return

    stop_words = {
        "the", "a", "an", "to", "in", "for", "of", "and", "on", "with", 
        "is", "at", "by", "from", "it", "as", "that", "its", "are", "be",
        "this", "was", "will", "has", "how", "why", "what", "about", "over"
    }

    words = []
    
    for item in data:
        title = item.get("title") or item.get("headline") or ""
        cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", title).lower()
        tokens = [w for w in cleaned.split() if w not in stop_words and len(w) > 2]
        words.extend(tokens)

    counts = Counter(words)
    top_10 = counts.most_common(10)

    print("\n--- 🚀 Top 10 Trending Keywords in Tech News ---")
    for word, count in top_10:
        print(f"• {word.capitalize()}: {count} mentions")

if __name__ == "__main__":
    analyze_headlines()