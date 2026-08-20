import json
import re
from collections import Counter


def analyze_headlines():
    file_path = "data/headlines.json"
    output_path = "data/trends.json"
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return

    # Filter out common filler words and generic terms
    stop_words = {
        "the", "a", "an", "to", "in", "for", "of", "and", "on", "with", 
        "is", "at", "by", "from", "it", "as", "that", "its", "are", "be",
        "this", "was", "will", "has", "how", "why", "what", "about", "over",
        "says", "app", "millions", "users", "face", "new", "more", "out"
    }

    words = []
    
    for item in data:
        title = item.get("title") or item.get("headline") or ""
        cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", title).lower()
        tokens = [w for w in cleaned.split() if w not in stop_words and len(w) > 2]
        words.extend(tokens)

    counts = Counter(words)
    top_10 = dict(counts.most_common(10))

    # Save final counts to data/trends.json
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(top_10, f, indent=2)

    print("\n--- 🚀 Top Trending Tech Keywords ---")
    for word, count in top_10.items():
        print(f"• {word.capitalize()}: {count} mentions")
    print(f"\nSaved results to {output_path}")

if __name__ == "__main__":
    analyze_headlines()  