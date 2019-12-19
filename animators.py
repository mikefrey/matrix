from time import time_ns
from typing import List

from app import App

class Rotator:
    '''
    Rotator rotates apps vertically on the screen
    '''
    def __init__(self, apps:List[App], duration:int, pauseLength:int):
        self.apps = apps
        self.duration = duration
        self.pauseLength = pauseLength
        self.paused = True
        self.pausedUntil = time_ns() + pauseLength
        self.animator = None

    def update(self, now:int, elapsed:int):
        if self.paused and self.pausedUntil < now:
            self.pausedUntil = 0
            self.paused = False

            start, finish = zip(*map(lambda a: (a.y, a.y-10), self.apps))
            self.animator = Animator(now, start, finish, self.duration)
        
        if self.paused:
            return

        y = self.animator.value(now)

        if self.animator.done:
            self.paused = True
            self.pausedUntil = now + self.pauseLength

        for i, app in enumerate(self.apps):
            app.y = y[i]
            if app.y <= -10:
                app.y = (len(self.apps)-1) * 10


class Scroller:
    '''
    Scrolls content right to left at the given speed
    '''
    def __init__(self, items, speed:int):
        pass


class Animator:
    def __init__(self, now:int, start, finish, duration:int):
        if not type(start) == type(finish):
            raise TypeError("start and finish must have the same type")
        self.start = start
        self.finish = finish
        self.duration = duration
        self.done = False
        self._startTick = now

        t = type(start)
        self._isList = t is list or t is tuple

        if self._isList:
            self._difference = [b - a for a, b in zip(start, finish)]
        else:
            self._difference = finish - start

    def value(self, tick_ns:int):
        elapsed = tick_ns - self._startTick
        scaler = min(elapsed / self.duration, 1.0)
        if scaler == 1.0:
            self.done = True
        if self._isList:
            return list(s + (scaler * d) for d, s in zip(self._difference, self.start))
        return self.start + (scaler * self._difference)

class Waiter:
    def __init__(self, until:int):
        self.until = until
    
    def isComplete(self, now:int) -> bool:
        return now > self.until
