from collections import UserDict

class FontBase(UserDict):
    def __init__(self, chars):
        # self.data = chars
        self.data = {}
        for k, v in chars.items():
            self.data[k] = self.__render(v)
    
    def measure(self, text):
        size = 0
        for c in text:
            size += len(self[c][0])
        return size

    def __getitem__(self, key):
        if key in self.data:
            # return self.__render(self.data[key])
            return self.data[key]
        print(f'missing character "{key}"')
        # return self.__render(self.data['?'])
        return self.data['?']

    def __render(self, charDef):
        width, char = charDef
        width += 1
        c = [
            [0]*width, 
            [0]*width, 
            [0]*width, 
            [0]*width, 
            [0]*width, 
            [0]*width, 
            [0]*width, 
            [0]*width,
        ]
        for y in range(0, 8):
            for x in range(0, width):
                p = char[y] & 1 << x
                c[y][x] = 1 if p else 0
        return c
