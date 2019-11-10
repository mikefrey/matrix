from framebuf import TranslatedFrameBuffer

class App:
    def __init__(self, instance, x:float, y:float):
        self.instance = instance
        self.x = x
        self.y = y

    def update(self, now:int, elapsed:int):
        self.instance.update(now, elapsed)

    def draw(self, fbuf):
        self.instance.draw(fbuf)