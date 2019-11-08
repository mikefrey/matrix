from time import time_ns
from img import Icon
from font5 import FontBase

class Set(dict):
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self._width = -1
        self.update()

    def __setitem__(self, key, item):
        self._width = -1
        dict.__setitem__(self, key, item)

    def draw(self, fbuf):
        for _, v in self.items():
            v.draw(fbuf, round(self.x), round(self.y))

    def width(self) -> int:
        if self._width > -1:
            return self._width
        width = 0
        for _, i in self.items():
            w = i.x + i.width()
            if w > width:
                width = w
        self._width = width
        return width

class Image:
    def __init__(self, img:Icon, x:int, y:int):
        self.x = x
        self.y = y
        self.img = img
        self.timeAtLastFrame = time_ns() // 1e6
        self.frame = 0

    def __setattr__(self, name, value):
        # When img is set to a new image, frame and timeAtLastFrame need to be
        # reset to avoid an out of range error. Not sure if this is the best
        # way to accomplish this or not.
        if name == "img" and "img" in self.__dict__ and self.__dict__["img"] != value:
            self.__dict__["frame"] = 0
            self.__dict__["timeAtLastFrame"] = time_ns() // 1e6
        self.__dict__[name] = value

    def draw(self, fbuf, offsetX:int=0, offsetY:int=0):
        now = time_ns() // 1e6
        duration = self.img.frames[self.frame].duration
        if now - self.timeAtLastFrame >= duration:
            self.frame = 0 if self.frame + 1 >= len(self.img.frames) else self.frame + 1
            self.timeAtLastFrame = now

        frameData = self.img.frames[self.frame].data
        fbuf.img(frameData, offsetX+self.x, offsetY+self.y, self.img.width, self.img.height)

    def width(self) -> int:
        return self.img.width

class Text:
    def __init__(self, font:FontBase, msg:str, x:float, y:float, color:int=0xffffff, align:str='left'):
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        self.msg = msg
        self.align = align

    def draw(self, fbuf, offsetX:int=0, offsetY:int=0):
        fbuf.text(self.font, self.msg, offsetX+round(self.x), offsetY+round(self.y), self.color, self.align)

    def width(self) -> int:
        return self.font.measure(self.msg)

class HLine:
    def __init__(self, x:int, y:int, l:int, color:int):
        self.x = x
        self.y = y
        self.color = color
        self.l = l

    def draw(self, fbuf, offsetX:int=0, offsetY:int=0):
        fbuf.vline(offsetX+self.x, offsetY+self.y, self.l, self.color)

    def width(self) -> int:
        return self.l

class VLine:
    def __init__(self, x:int, y:int, l:int, color:int):
        self.x = x
        self.y = y
        self.color = color
        self.l = l

    def draw(self, fbuf, offsetX:int=0, offsetY:int=0):
        fbuf.vline(offsetX+self.x, offsetY+self.y, self.l, self.color)

    def width(self) -> int:
        return 1
