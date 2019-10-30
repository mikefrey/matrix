import abc

class Image:
    def __init__(self, img, x, y):
        self.x = x
        self.y = y
        self.img = img

    def draw(self, fbuf):
        fbuf.img(self.img.data, self.x, self.y, self.img.width, self.img.height)

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
