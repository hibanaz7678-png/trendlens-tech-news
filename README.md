# TrendLens Tech News

A Python data pipeline that fetches TechCrunch news headlines via Bright Data and extracts trending technology topics.

## Features

- **Data Scraping:** Downloads snapshot data in NDJSON/JSON format (`fetch_news.py`).
- **Trend Analysis:** Filters out stop-words and outputs top tech keywords (`analyze_trends.py`).

## Bright Data Scraper Studio

TrendLens uses a custom Bright Data Scraper Studio scraper to collect public technology-news headlines.

**Collector ID:** `c_mszt0gix2gv5jy0b49`

The scraper returns structured headline records. The Python pipeline saves them in `data/headlines.json`, then analyzes the words and writes `data/trends.json`.

This project uses a custom scraper for TechCrunch, which is not available in Bright Data’s pre-built Scraper Library.

## How to Run

1. Install dependencies:
   ```bash
   pip install requests
   ```

2. Replace `YOUR_API_KEY_HERE` in `fetch_news.py` with your real Bright Data API key.

3. Fetch headlines:
   ```bash
   python fetch_news.py
   ```
   This creates `data/headlines.json`.

4. Analyze trends:
   ```bash
   python analyze_trends.py
   ```
   This creates `data/trends.json` and prints the top keywords to the terminal.

## Output

- `data/headlines.json` — Raw headline records from TechCrunch.
- `data/trends.json` — Top 10 trending technology keywords and their mention counts.

## AI-use disclosure

AI coding assistants were used to help with development and debugging. I reviewed, tested, and understand the scraping flow, JSON storage, keyword filtering, and trend-analysis logic.

## Self-healing (future work)

This version uses a custom Bright Data scraper but does not yet demonstrate the self-healing workflow. Future versions will use `bdata scraper heal` to repair the scraper when the site layout changes.

Example command:
```bash
bdata scraper heal c_mszt0gix2gv5jy0b49 "The headline title is no longer extracting. Find the current headline elements and restore title and article_url extraction."
```
```