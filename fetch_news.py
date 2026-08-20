import os
import json
import requests

# Configuration
API_KEY = "BRIGHTDATA_API_KEY"
SNAPSHOT_ID = "j_mszx14o9266j4shfd2"

def fetch_and_save_data():
    os.makedirs("data", exist_ok=True)
    
    url = f"https://api.brightdata.com/dca/dataset?id={SNAPSHOT_ID}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    print("Fetching records from Bright Data snapshot...")
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print(response.text)
        return

    # Parse JSON Lines format (NDJSON)
    data = [json.loads(line) for line in response.text.strip().split("\n") if line]
    print(f"Successfully retrieved {len(data)} records!")

    output_file = "data/headlines.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"Saved dataset to {output_file}")

if __name__ == "__main__":
    fetch_and_save_data()

