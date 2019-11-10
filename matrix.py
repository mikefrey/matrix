import time
import signal
import sys

import board
import neopixel

from app import App
from framebuf import FrameBuffer, TranslatedFrameBuffer
from timer import Timer, Animator

from apps.clock.clock import Clock
from apps.weather.weather import Weather
from apps.news.news import News


class Matrix:
    def __init__(self, width, height, channels, brightness=1):
        self.running = False
        self.width = width
        self.height = height
        self.channels = channels

        self.pixels = neopixel.NeoPixel(board.D18, width*height, bpp=channels, brightness=brightness, auto_write=False)

        buf1 = bytearray(width * height * channels)
        # buf2 = bytearray(width * height * channels)
        self.fbuf = FrameBuffer(buf1, width, height, channels)
        # self.bbuf = FrameBuffer(buf2, width, height, channels)
        self.tbuf = TranslatedFrameBuffer(self.fbuf, 0, 0)

        self.apps = [
            App(News(), 0, 0),
            App(Weather(), 0, 10),
            App(Clock(), 0 , 20)
        ]

        self.timer = Timer(self.loop, 60)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()
        self.pixels.fill(0x000000)
        self.pixels.show()

    def update(self, now:int, elapsed:int):
        self.fbuf.clear()

        for app in self.apps:
            app.update(now, elapsed)
            app.y = app.y - elapsed/1e9 * 3
            if round(app.y) < -7:
                app.y = app.y + len(self.apps) * 10

    def draw(self):
        for app in self.apps:
            if -7 < app.x and app.x < 8:
                self.tbuf.tx = app.x
                self.tbuf.ty = app.y
                app.draw(self.tbuf)

        for i in range(self.width * self.height):
            x = i // self.height
            y = i % self.height

            if x % 2:
                # reverse direction for y
                y = (self.height-1) - y

            color = self.fbuf.get(x, y)
            self.pixels[i] = color

    def loop(self, now, elapsed):
        self.update(now, elapsed)
        self.draw()
        self.pixels.show()


# matrix = Matrix(64, 8, 3, 0.05)
matrix = Matrix(64, 8, 3, 0.05)

def sigHandler(signum, frame):
    matrix.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, sigHandler)

matrix.start()
