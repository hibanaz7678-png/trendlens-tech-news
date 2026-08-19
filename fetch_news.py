import requests
import time
from collections import Counter
import re

API_TOKEN = "80ae45a7-f3c5-4733-8fd1-b497d59d375c"
COLLECTOR_ID = "c_mszt0gix2gv5jy0b49"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# 1. Trigger the collector job
trigger_url = f"https://api.brightdata.com/dca/trigger?collector={COLLECTOR_ID}&queue_next=1"
res = requests.post(trigger_url, headers=headers, json=[{}])
job_data = res.json()
collection_id = job_data.get("collection_id")

print(f"Triggered Job ID: {collection_id}")

if not collection_id:
    print("Error: Could not retrieve collection_id from response:", job_data)
    exit()

# 2. Poll Bright Data until the dataset is ready
dataset_url = f"https://api.brightdata.com/dca/dataset?id={collection_id}"
print("Waiting for collector to complete processing...")

results = []
max_retries = 12  # Poll for up to 2 minutes (12 attempts * 10 seconds)

for attempt in range(max_retries):
    time.sleep(10)
    data_res = requests.get(dataset_url, headers=headers)
    
    try:
        data = data_res.json()
        if isinstance(data, list) and len(data) > 0:
            results = data
            print(f"Data retrieved successfully on attempt {attempt + 1}!")
            break
    except Exception:
        pass

    print(f"Still processing... (attempt {attempt + 1}/{max_retries})")

print("\n--- Raw Results ---")
print(results)

# 3. Basic Trend / Keyword Analysis
if isinstance(results, list) and len(results) > 0:
    all_titles = " ".join([item.get("title", "") for item in results if isinstance(item, dict)])
    words = re.findall(r'\w+', all_titles.lower())
    
    # Exclude common stop words
    stop_words = {"the", "a", "and", "to", "of", "in", "for", "is", "on", "that", "by", "this", "with"}
    filtered_words = [w for w in words if w not in stop_words and len(w) > 2]
    
    print("\n--- Top Trending Keywords ---")
    for word, count in Counter(filtered_words).most_common(10):
        print(f"{word}: {count}")
else:
    print("\nNo dataset returned. Check your Bright Data collector dashboard to verify the scraper logic.")