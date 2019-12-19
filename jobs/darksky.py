import threading
import time

from config import dark_sky_key, dark_sky_lat, dark_sky_lon
from darksky.api import DarkSky, Forecast

class WeatherFetcher:
    def __init__(self):
        self.data:Forecast = None
        self._lock = threading.Lock()
        self.darksky = DarkSky(dark_sky_key)

    def do(self):
        forecast = self.darksky.get_forecast(dark_sky_lat, dark_sky_lon)
        self.update(forecast)
        print(forecast.currently.temperature)


    def update(self, data:Forecast):
        with self._lock:
            self.data = data

    def read(self):
        with self._lock:
            return self.data
