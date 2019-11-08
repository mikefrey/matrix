from pathlib import Path
from datetime import datetime
from math import floor
import time
import threading

from newsapi import NewsApiClient

import drawable
from font5 import Font5
from img import Icon

key = ''
sources = 'the-new-york-times,the-wall-street-journal,bbc-news,abc-news,al-jazeera-english'
sourceMap = {
    'the-new-york-times': 'NYT',
    'the-wall-street-journal': 'WSJ',
    'bbc-news': 'BBC',
    'abc-news': 'ABC',
    'al-jazeera-english': 'AJE',
}

class News:
    def __init__(self):
        # start the fetcher thread
        self.fetcher = NewsFetcher()
        self.worker = threading.Thread(target=self.fetcher.start, daemon=True)
        self.worker.start()

        self.lastUpdate = 0

        self.items = {}

    def fillSet(self, news, lastUpdate):
        x = 64
        if self.lastUpdate in self.items.items():
            # measure width of prev set to get the x offset for the next set.
            prev = self.items[self.lastUpdate]
            x = prev.width() + prev.x + 64

        newsSet = drawable.Set(x, 0)
        self.items[lastUpdate] = newsSet
        xx = 0
        for article in news:
            source = article.source
            title = article.title
            newsSet[xx] = drawable.Text(Font5, source, xx, 0, 0xff0000, 'left')
            xx = xx + Font5.measure(source) + 4
            newsSet[xx] = drawable.Text(Font5, title, xx, 0, 0xdddddd, 'left')
            xx = xx + Font5.measure(title) + 20


    def update(self, now:int, elapsed:int):
        news, lastUpdate = self.fetcher.read()
        if (not news):
            return

        if lastUpdate > self.lastUpdate:
            self.fillSet(news, lastUpdate)
            self.lastUpdate = lastUpdate

        for k, v in self.items.items():
            if k != self.lastUpdate and v.x + v.width() < 0:
                del self.items[k]
            elif v.x + v.width() < 0:
                v.x = 64
            else:
                v.x = v.x - elapsed/1e9*10



        # item = self.items['1']
        # if not title == item.msg:
        #     item.msg = title
        #     item.x = 10
        # elif item.x + Font5.measure(item.msg) < 0:
        #     item.x = 64
        # else:
        #     item.x = item.x - elapsed/1e9 * 10
        
    def draw(self, fbuf):
        for _, v in self.items.items():
            v.draw(fbuf)

class NewsFetcher:
    def __init__(self):
        self.data = None
        self.lastUpdate = None
        self._lock = threading.Lock()
        self.newsapi = NewsApiClient(api_key=key)

    def start(self):
        print("starting news fetcher...")
        while True:
            news = self.newsapi.get_top_headlines(sources=sources, page_size=5)
            self.update(news)
            time.sleep(5*60)


    def update(self, data):
        articles = []
        for article in data["articles"]:
            articles.append(Article(article))
        with self._lock:
            self.data = articles
            self.lastUpdate = time.time()

    def read(self):
        with self._lock:
            return self.data, self.lastUpdate

class Article:
    def __init__(self, article):
        self.source = sourceMap[article["source"]["id"]]
        self.title = article["title"]
        self.publishedAt = article["publishedAt"]