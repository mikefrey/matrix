from pathlib import Path
from datetime import datetime
import drawable
from font5 import Font5
from img import Icon

class Clock:
    def __init__(self):
        # load the icon
        icon = Icon(Path('apps/clock/clock.png'))
        icon.read()
        
        items = {}

        items['image'] = drawable.Image(icon, 0, 0)
        items['time'] = drawable.Text(Font5, '00:00AM', 10+28, 0, 0xffffff, 'right')
        items['date'] = drawable.Text(Font5, '', 1, 1, 0x000000)

        self.items = items

    def update(self, now:int, elapsed:int):
        now = datetime.now()
        self.items['time'].msg = now.strftime('%I:%M%p').lstrip('0')
        self.items['date'].msg = now.strftime('%d')

    def draw(self, fbuf):
        for _, v in self.items.items():
            v.draw(fbuf)
