from PIL import Image

class Frame:
    def __init__(self, data, duration):
        self.data = data
        self.duration = duration

class Icon:
    def __init__(self, path):
        self.path = path
        self.frames = []

    def read(self):
        with Image.open(self.path) as frame:
            self.width = frame.width
            self.height = frame.height

            palette = frame.getpalette()

            i = 0
            while frame:
                duration = 1000
                if 'duration' in frame.info:
                    duration = frame.info['duration']
                    print(f"{self.path} - frame {i} - {duration} {type(duration)}")
                
                data = list(frame.getdata())
                if palette:
                    newdata = []
                    for d in data:
                        newdata.append(tuple(palette[d*3:d*3+3]))
                    data = newdata

                self.frames.append(Frame(data, duration))
                i += 1

                try:
                    frame.seek(i)
                except EOFError:
                    break
