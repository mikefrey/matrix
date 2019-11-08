from pathlib import Path
from datetime import datetime
import http.client
import time
import threading

from darksky.api import DarkSky, Forecast

import drawable
from font5 import Font5
from img import Icon

key = ''
lat = '45.1204118'
lon = '-93.2150891'

icons = {
    "clear-day": Icon(Path('apps/weather/weather-clear-day.gif')),
    "clear-night": Icon(Path('apps/weather/weather-clear-night.gif')),
    "rain": Icon(Path('apps/weather/weather-rain.gif')),
    "snow": Icon(Path('apps/weather/weather-snow.gif')),
    "sleet": Icon(Path('apps/weather/weather-sleet.gif')),
    "wind": Icon(Path('apps/weather/weather-wind.gif')),
    "fog": Icon(Path('apps/weather/weather-fog.gif')),
    "cloudy": Icon(Path('apps/weather/weather-cloudy.gif')),
    "partly-cloudy-day": Icon(Path('apps/weather/weather-partly-cloudy-day.gif')),
    "partly-cloudy-night": Icon(Path('apps/weather/weather-partly-cloudy-night.gif')),
    "default": Icon(Path('apps/weather/weather-partly-cloudy-day.gif')),
}

class Weather:
    def __init__(self):
        # start the fetcher thread
        self.fetcher = WeatherFetcher()
        self.worker = threading.Thread(target=self.fetcher.start, daemon=True)
        self.worker.start()

        # load the icons
        for _, icon in icons.items():
            icon.read()

        icon = icons["default"]

        currentX = Font5.measure("100°F") + 9
        highX = Font5.measure(" 100°") + currentX
        lowX = Font5.measure(" 00°") + highX
        
        items = {}

        items['image'] = drawable.Image(icon, 0, 0)
        items['current'] = drawable.Text(Font5, '0°F', currentX, 0, 0xffffff, 'right')
        items['high'] = drawable.Text(Font5, '0°', highX, 0, 0xff5555, 'right')
        items['low'] = drawable.Text(Font5, '0°', lowX, 0, 0x5555ff, 'right')

        self.items = items

    def update(self, now:int, elapsed:int):
        forecast = self.fetcher.read()
        if (not forecast):
            return

        iconName = forecast.currently.icon
        if not iconName in icons:
            iconName = "default"

        self.items['image'].img = icons[iconName]
        self.items['current'].msg = "{:3.0f}".format(forecast.currently.temperature) + "°F"
        # self.items['high'].msg = "{:3.0f}".format(forecast.daily.data[0].temperatureHigh) + "°"
        self.items['high'].msg = f"{forecast.daily.data[0].temperature_high:.0f}°"
        self.items['low'].msg = f"{forecast.daily.data[0].temperature_low:.0f}°"

    def draw(self, fbuf):
        for _, v in self.items.items():
            v.draw(fbuf)

class WeatherFetcher:
    def __init__(self):
        self.data:Forecast = None
        self._lock = threading.Lock()
        self.darksky = DarkSky(key)

    def start(self):
        print("starting weather fetcher...")
        while True:
            forecast = self.darksky.get_forecast(lat, lon)
            print(f"{forecast.currently.temperature} {forecast.currently.icon}")
            self.update(forecast)
            time.sleep(5*60)


    def update(self, data:Forecast):
        with self._lock:
            self.data = data

    def read(self):
        with self._lock:
            return self.data
