import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from urllib.parse import quote
import pandas as pd

search_terms = [
    "solar energy",
    "solar panels",
    "solar power",
    "solar technology"
]

articles = {}

for term in search_terms:
    url = (
        "https://news.google.com/rss/search?q="
        + quote(term + " when:1d")
        + "&hl=en-US&gl=US&ceid=US:en"
    )

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    root = ET.fromstring(response.content)

    for item in root.findall(".//item"):
        title = item.findtext("title", "")
        link = item.findtext("link", "")
        date = item.findtext("pubDate", "")

        articles[link or title] = {
            "title": title,
            "date": date
        }

print("Found", len(articles), "unique articles")
