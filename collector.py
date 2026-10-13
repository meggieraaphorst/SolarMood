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

from transformers import pipeline

# Load our pretrained AI model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    device=-1
)

# Test the model with the first 5 articles
for article in list(articles.values())[:5]:
    prediction = sentiment_model(
        article["title"],
        truncation=True
    )[0]

    print("Article:", article["title"])
    print("Sentiment:", prediction["label"])
    print("Confidence:", round(prediction["score"], 2))
    print()
