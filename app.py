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

# class AppManager:
#     def __init__(self):
#         self.apps = []
#         self.appHeight = 10

#     def add(self, app):
#         self.apps.append(App(app, 0, len(self.apps)*self.appHeight))

#     def update(self, now:int, elapsed:int):
#         pass

    