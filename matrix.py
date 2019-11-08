import time
import signal
import sys

import board
import neopixel

import font5
import framebuf
import img
from timer import Timer

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

        buf = bytearray(width * height * channels)
        self.fbuf = framebuf.FrameBuffer(buf, width, height, channels)

        self.apps = [
            News(),
            Weather(),
            Clock()
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

        app = self.apps[0]
        app.update(now, elapsed)

    def draw(self):
        app = self.apps[0]
        app.draw(self.fbuf)

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
matrix = Matrix(64, 8, 3, 0.5)

def sigHandler(signum, frame):
    matrix.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, sigHandler)

matrix.start()
