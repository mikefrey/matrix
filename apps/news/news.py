import drawable
from fonts.font5 import Font5
from img import Icon

class News:
    def __init__(self, fetcher):
        self.fetcher = fetcher
        self.lastUpdate = 0.0
        self.items = {}

    def fillSet(self, news, lastUpdate):
        x = 64
        if self.lastUpdate in self.items.keys():
            # measure width of prev set to get the x offset for the next set.
            prev = self.items[self.lastUpdate]
            x = prev.x + prev.width() + 64

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

        toDelete = None
        for k, v in self.items.items():
            if k != self.lastUpdate and v.x + v.width() < 0:
                toDelete = k
            elif v.x + v.width() < 0:
                v.x = 64
            else:
                v.x = v.x - elapsed/1e9*14

        if toDelete:
            del self.items[toDelete]

        
    def draw(self, fbuf):
        for _, v in self.items.items():
            v.draw(fbuf)
