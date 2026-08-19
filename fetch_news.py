#80ae45a7-f3c5-4733-8fd1-b497d59d375c

import requests

API_TOKEN = "80ae45a7-f3c5-4733-8fd1-b497d59d375c"
COLLECTOR_ID = "c_mszt0gjx2gv5jy0b49"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Trigger the collector job
url = f"https://api.brightdata.com/dca/trigger?collector={COLLECTOR_ID}&queue_next=1"
response = requests.post(url, headers=headers, json=[{}])

print("Status Code:", response.status_code)
print("Response:", response.json())