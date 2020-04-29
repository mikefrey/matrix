import signal
import sys
import threading
import time

import board
import neopixel

from animators import Rotator
from app import App
from framebuf import FrameBuffer, TranslatedFrameBuffer
from surface import Surface
from timer import Timer

from apps.clock.clock import Clock
from apps.weather.weather import Weather
from apps.news.news import News

from jobs.darksky import WeatherFetcher
from jobs.newsapi import NewsApi

import config

second = 1e9
ms = 1e6

class JobRunner:
    def __init__(self):
        self.fns = []
        self.worker = threading.Thread(target=self.do, daemon=True)

    def add(self, fn):
        self.fns.append(fn)

    def start(self):
        self.worker.start()

    def do(self):
        while True:
            for fn in self.fns:
                fn()
            time.sleep(5*60)

class Matrix:
    def __init__(self, width, height, channels, brightness=1):
        self.running = False
        self.width = width
        self.height = height
        self.channels = channels
        self.tbuf = TranslatedFrameBuffer()

        self.surface = Surface(width, height, channels, brightness)

        self.jobs = JobRunner()

        weatherFetcher = WeatherFetcher()
        newsApi = NewsApi()

        self.jobs.add(weatherFetcher.do)
        self.jobs.add(newsApi.do)

        self.apps = [
            App(News(newsApi), 0, 0),
            App(Weather(weatherFetcher), 0, 10),
            App(Clock(), 0, 20),
        ]

        self.rotator = Rotator(self.apps, 2*second, 120*second)
        self.timer = Timer(self.loop, 60)
    
    def start(self):
        print('starting...')
        self.jobs.start()
        self.timer.start()

    def stop(self):
        self.timer.stop()
        self.surface.dispose()

    def update(self, now:int, elapsed:int):
        self.rotator.update(now, elapsed)

        for app in self.apps:
            app.update(now, elapsed)

    def draw(self):
        fbuf = self.surface.begin()

        try:
            fbuf.clear()

            self.tbuf.fbuf = fbuf

            for app in self.apps:
                if -7 < app.x and app.x < 8:
                    self.tbuf.tx = app.x
                    self.tbuf.ty = app.y
                    app.draw(self.tbuf)
        except:
            print("Unexpected error:", sys.exc_info()[0])
        finally:
            self.surface.commit()

    def loop(self, now, elapsed):
        self.update(now, elapsed)
        self.draw()
        # print('loop')
        time.sleep(0.001)

def main():
    # matrix = Matrix(64, 8, 3, 0.05)
    matrix = Matrix(64, 8, 3, 0.05)

    def sigHandler(signum, frame):
        matrix.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, sigHandler)

    matrix.start()

if __name__ == "__main__":
    main()
