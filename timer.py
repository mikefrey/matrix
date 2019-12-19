from time import time_ns, sleep
from typing import Callable

class Timer:
    def __init__(self, loopFn:Callable[[int, int], None], fps:int):
        self.loopFn = loopFn
        self.fps = fps
        self._running = False
        self.lastTick = time_ns()
        self.nsPerFrame = 1e9 // fps

    def start(self) -> None:
        self._running = True
        while self._running:
            now = time_ns()
            elapsed = now - self.lastTick
            self.lastTick = now
            # print(1e9//elapsed, "fps")
            
            self.loopFn(now, elapsed)

            # loopTime = self.nsPerFrame - time_ns()
            # remainingTime = self.nsPerFrame - (time_ns() - now)
            # if remainingTime > 0:
            #     sleep(remainingTime/1e9)

    def stop(self) -> None:
        self._running = False
        