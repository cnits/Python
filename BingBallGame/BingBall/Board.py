# __author__ = 'PhongVu'
import BBConfig as bbc
try:
    from Tkinter import *
except:
    from tkinter import *


class Board(Canvas):
    def __init__(self, parent):
        _width = parent.winfo_screenwidth() - bbc.MIN_W
        _height = parent.winfo_screenheight() - bbc.MIN_H
        if _width < bbc.MIN_W:
            _width = bbc.MIN_W
        if _height < bbc.MIN_H:
            _height = bbc.MIN_H

        Canvas.__init__(
            self, parent, width=_width, height=_height,
            background=bbc.BOARD_COLOR, highlightthickness=0
        )

        self.parent = parent
        self.pack(fill=BOTH, expand=1)
