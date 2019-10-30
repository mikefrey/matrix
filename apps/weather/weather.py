from pathlib import Path
from datetime import datetime
import http.client
import time
import threading

from darksky.api import DarkSky

import drawable
from font5 import Font5
from img import Icon

key = ''
lat = '45.1204118'
lon = '-93.2150891'

class Weather:
    def __init__(self):
        # start the fetcher thread
        self.fetcher = WeatherFetcher()
        self.worker = threading.Thread(target=self.fetcher.start, daemon=True)
        self.worker.start()

        # load the icon
        # icon = Icon(Path('apps/weather/weather.png'))
        # icon.read()
        
        items = {}

        # items['image'] = drawable.Image(icon, 0, 0)
        items['current'] = drawable.Text(Font5, '0°F', 10+19, 0, 0xffffff, 'right')

        self.items = items

    def update(self):
        forecast = self.fetcher.read()
        if (not forecast):
            return
        self.items['current'].msg = "{:3.0f}".format(forecast.currently.temperature) + "°F"

    def draw(self, fbuf):
        for _, v in self.items.items():
            v.draw(fbuf)

class WeatherFetcher:
    def __init__(self):
        self.data = False
        self._lock = threading.Lock()
        self.darksky = DarkSky(key)

    def start(self):
        print("starting...")
        while True:
            forecast = self.darksky.get_forecast(lat, lon)
            print(forecast.currently.temperature)
            self.update(forecast)
            time.sleep(5*60)


    def update(self, data):
        with self._lock:
            self.data = data

    def read(self):
        with self._lock:
            return self.data
