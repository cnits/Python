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
        self.bar_pos = bbc.BAR_T

        self.parent = parent
        self.pack(fill=BOTH, expand=1)

    def set_ball_name(self, name):
        self.ball = name

    def get_ball_name(self):
        return self.ball

    def set_bar_r_name(self, name):
        self.barR = name

    def get_bar_r_name(self):
        return self.barR

    def set_bar_g_name(self, name):
        self.barG = name

    def get_bar_g_name(self):
        return self.barG

    def put_bar_pos(self, pos):
        self.bar_pos = pos

    def get_bar_pos(self):
        return self.bar_pos
