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


class Animator:
    def __init__(self, start, finish, duration:int):
        if not type(start) == type(finish):
            raise TypeError("start and finish must have the same type")
        self.start = start
        self.finish = finish
        self.duration = duration * 1e6
        self._startTick = time_ns()

        t = type(start)
        self._isList = t is list or t is tuple

        if self._isList:
            self._difference = [b - a for a, b in zip(start, finish)]
        else:
            self._difference = finish - start

    def value(self, tick_ns:int):
        scaler = min(self.duration / (tick_ns - self._startTick), 1.0)
        if self._isList:
            return list(s + (scaler * d) for d, s in zip(self._difference, self.start))
        return self.start + (scaler * self._difference)