import threading
import time

from config import news_api_key, news_api_sources
from newsapi import NewsApiClient

key = news_api_key
sources = news_api_sources
sourceMap = {
    'the-new-york-times': 'NYT',
    'the-wall-street-journal': 'WSJ',
    'bbc-news': 'BBC',
    'abc-news': 'ABC',
    'al-jazeera-english': 'AJE',
}

class NewsApi:
    def __init__(self):
        self.data = None
        self.lastUpdate = None
        self._lock = threading.Lock()
        self.newsapi = NewsApiClient(api_key=key)

    def do(self):
        news = self.newsapi.get_top_headlines(sources=sources, page_size=5)
        self.update(news)

    def update(self, data):
        articles = []
        for article in data["articles"]:
            articles.append(Article(article))
        with self._lock:
            self.data = articles
            self.lastUpdate = time.time()

    def read(self) -> (list, float):
        with self._lock:
            return self.data, self.lastUpdate

class Article:
    def __init__(self, article):
        self.source = sourceMap[article["source"]["id"]]
        self.title = article["title"]
        self.publishedAt = article["publishedAt"]
