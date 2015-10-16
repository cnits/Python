# __author__ = 'PhongVu'
from Tkinter import *


class Board(Canvas):
    def __init__(self, parent, _width, _height, color):
        Canvas.__init__(
            self, parent, width=_width, height=_height,
            background=color, highlightthickness=0
        )
        self.parent = parent
        self.width = _width
        self.height = _height
        self.color = color
        self.pack(fill=BOTH, expand=1)
