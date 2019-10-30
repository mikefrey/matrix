from PIL import Image

class Icon:
    def __init__(self, path):
        self.path = path

    def read(self):
        with Image.open(self.path) as i:
            data = list(i.getdata())

            self.width = i.width
            self.height = i.height
            self.data = data
