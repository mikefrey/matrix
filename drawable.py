import abc
from time import time_ns

class Image:
    def __init__(self, img, x, y):
        self.x = x
        self.y = y
        self.img = img
        self.timeAtLastFrame = time_ns() // 1000000
        self.frame = 0

    def draw(self, fbuf):
        now = time_ns() // 1000000
        duration = self.img.frames[self.frame].duration
        if now - self.timeAtLastFrame >= duration:
            self.frame = 0 if self.frame + 1 >= len(self.img.frames) else self.frame + 1
            self.timeAtLastFrame = now

        frameData = self.img.frames[self.frame].data
        fbuf.img(frameData, self.x, self.y, self.img.width, self.img.height)

class Text:
    def __init__(self, font, msg, x, y, color=0xffffff, align='left'):
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        self.msg = msg
        self.align = align

    def draw(self, fbuf):
        fbuf.text(self.font, self.msg, self.x, self.y, self.color, self.align)

class HLine:
    def __init__(self, x, y, l, color):
        self.x = x
        self.y = y
        self.color = color
        self.l = l

    def draw(self, fbuf):
        fbuf.vline(self.x, self.y, self.l, self.color)

class VLine:
    def __init__(self, x, y, l, color):
        self.x = x
        self.y = y
        self.color = color
        self.l = l

    def draw(self, fbuf):
        fbuf.vline(self.x, self.y, self.l, self.color)
