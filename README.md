# TrendLens Tech News

A Python data pipeline that fetches TechCrunch news headlines via Bright Data and extracts trending technology topics.

## Features
- **Data Scraping:** Downloads snapshot data in NDJSON/JSON format (`fetch_news.py`).
- **Trend Analysis:** Filters out stop-words and outputs top tech keywords (`analyze_trends.py`).

## How to Run
1. Install dependencies:
   ```bash
   pip install requests
