import threading
import time

import board
import neopixel

from framebuf import FrameBuffer, TranslatedFrameBuffer

class Surface:
    def __init__(self, width, height, channels, brightness=1):
        self.height = height
        self.width = width
        self.channels = channels
        
        self.pixels = neopixel.NeoPixel(board.D18, width*height, bpp=channels, brightness=brightness, auto_write=False)

        self.frameBuffers = (
            FrameBuffer(bytearray(width * height * channels), width, height, channels),
            FrameBuffer(bytearray(width * height * channels), width, height, channels)
        )

        self.activeLock = threading.Lock()
        self.active = 0
        self.inactive = 1

        self.worker = threading.Thread(target=self.__write, daemon=True)
        self.worker.start()
    
    def dispose(self):
        self.pixels.fill(0x000000)
        self.pixels.show()

    def begin(self) -> FrameBuffer:
        # print('main waiting')
        self.activeLock.acquire()
        # print('main acquired')
        return self.frameBuffers[self.active]

    def commit(self):
        self.activeLock.release()
        # print('main released')

    def __write(self):
        while True:
            fbuf = self.frameBuffers[self.inactive]
            for i in range(self.width * self.height):
                x = i // self.height
                y = i % self.height

                if x % 2:
                    # reverse direction for y
                    y = (self.height-1) - y

                self.pixels[i] = fbuf.get(x, y)
            
            # print('__write')        
            self.pixels.show()

            with self.activeLock:
                self.active, self.inactive = (self.inactive, self.active)

            time.sleep(0.01)
