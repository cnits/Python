# __author__ = 'PhongVu'
from Tkinter import *


class Ball:
    def __init__(self, fx, fy, lx, ly, color):
        self.fx, self.fy, self.lx, self.ly = fx, fy, lx, ly
        self.color = color

    def set_coord(self, fx, fy, lx, ly):
        self.fx, self.fy, self.lx, self.ly = fx, fy, lx, ly

    def set_color(self, color):
        self.color = color

    def reset_coord(self):
        self.fx, self.fy, self.lx, self.ly = 0, 0, 0, 0

    def get_coord(self):
        return self.fx, self.fy, self.lx, self.fy

    def get_color(self):
        return self.color
