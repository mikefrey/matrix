from math import floor

class FrameBuffer:

    def __init__(self, buf, width, height, channels=3):
        self.buf = buf
        self.width = width
        self.height = height
        self.channels = channels
        self.stride = channels * width
        self.brightness = 1.0

    def pixel(self, x, y, color=(0x000000)):
        if x < 0 or self.width <= x:
            return
        if y < 0 or self.height <= y:
            return
        index = (y * self.stride) + (x * self.channels)
        
        t = type(color)
        if t is int:
            r = color >> 16
            g = (color >> 8) & 0xff
            b = color & 0xff
        elif t is tuple:
            r, g, b = color
        else:
            return
        
        self.buf[index + 0] = r
        self.buf[index + 1] = g
        self.buf[index + 2] = b

    def get(self, x, y):
        i = (y * self.stride) + (x * self.channels)
        r = floor(self.buf[i] * self.brightness)
        g = floor(self.buf[i+1] * self.brightness)
        b = floor(self.buf[i+2] * self.brightness)
        return ((r << 16) | (g << 8) | b)

    def clear(self):
        """Turns all the pixels to black"""
        for i in range(len(self.buf)):
            self.buf[i] = 0
    
    def char(self, char, x, y, color=0xffffff):
        """
        Writes a character to the buffer at x, y in the given color.

        char must be a matrix of 0 (off) or 1 (on)
        """
        # print(char)
        for yy, row in enumerate(char):
            for xx, px in enumerate(row):
                if px == 1:
                    self.pixel(x+xx, y+yy, color)
        return x + len(char[0])
    
    def text(self, font, msg, x, y, color=0xffffff, align='left'):
        """
        draws a string of characters
        """
        if align == 'right':
            l = font.measure(msg)
            x -= l
        if align == 'center':
            l = font.measure(msg)
            x -= l // 2

        for char in msg:
            w = len(font[char][0])
            if x+w > 0 and x < self.width:
                self.char(font[char], x, y, color)
            x = x+w
        return x
    
    def img(self, img, x, y, w, h):
        """
        draws a simple bitmap buffer to the framebuffer
        """
        for i, px in enumerate(img):
            yy = y + i // w
            xx = x + i % w
            self.pixel(xx, yy, px)

    def vline(self, x, y, l, color=0xffffff):
        """
        draws a vertical line l pixels long
        """
        for i in range(l):
            self.pixel(x, y+i, color)

    def hline(self, x, y, l, color=0xffffff):
        """
        draws a horizontal line l pixels long
        """
        for i in range(l):
            self.pixel(x+i, y, color)

class TranslatedFrameBuffer:
    def __init__(self, fbuf, tx, ty):
        self.fbuf = fbuf
        self.tx = tx
        self.ty = ty
        
    def pixel(self, x, y, color=(0x000000)):
        x = round(self.tx + x)
        y = round(self.ty + y)
        return self.fbuf.pixel(x, y, color)

    def get(self, x, y):
        x = round(self.tx + x)
        y = round(self.ty + y)
        return self.fbuf.get(x, y)

    def clear(self):
        return self.fbuf.clear()
    
    def char(self, char, x, y, color=0xffffff):
        x = round(self.tx + x)
        y = round(self.ty + y)
        return self.fbuf.char(char, x, y, color)
    
    def text(self, font, msg, x, y, color=0xffffff, align='left'):
        x = round(self.tx + x)
        y = round(self.ty + y)
        return self.fbuf.text(font, msg, x, y, color, align)
    
    def img(self, img, x, y, w, h):
        x = round(self.tx + x)
        y = round(self.ty + y)
        return self.fbuf.img(img, x, y, w, h)

    def vline(self, x, y, l, color=0xffffff):
        x = round(self.tx + x)
        y = round(self.ty + y)
        return self.fbuf.vline(x, y, l, color)

    def hline(self, x, y, l, color=0xffffff):
        x = round(self.tx + x)
        y = round(self.ty + y)
        return self.fbuf.hline(x, y, l, color)
