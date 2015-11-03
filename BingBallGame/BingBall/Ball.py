# __author__ = 'PhongVu'
import math
import random


class Ball:
    def __init__(self, container_width, container_height, color):
        temp = container_height
        if container_width < container_height:
            temp = container_width
        self.d = math.floor(temp/10)

        self.fx = random.randint(0, container_width - 2*self.d)
        self.fy = random.randint(0, container_height - 2*self.d)
        self.lx = self.fx + self.d
        self.ly = self.fy + self.d
        self.color = color

    def set_coord(self, fx, fy, lx, ly):
        self.fx, self.fy, self.lx, self.ly = fx, fy, lx, ly

    def set_color(self, color):
        self.color = color

    def reset_coord(self):
        self.fx, self.fy, self.lx, self.ly = 0, 0, 0, 0

    def get_coord(self):
        return self.fx, self.fy, self.lx, self.ly

    def get_color(self):
        return self.color
