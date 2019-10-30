class FrameBuffer:

    def __init__(self, buf, width, height):
        self.buf = buf
        self.width = width
        self.height = height
        self.stride = 3 * width

    def pixel(self, x, y, color=(0x000000)):
        index = (y * self.stride) + (x * 3)
        if index+2 > len(self.buf):
            return
        
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
        i = (y * self.stride) + (x * 3)
        # if i + 2 > len(self.buf):
        #     return 0x000000
        return ((self.buf[i] << 16) | (self.buf[i+1] << 8) | self.buf[i+2])

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
            x = self.char(font[char], x, y, color)
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
