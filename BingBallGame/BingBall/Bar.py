# __author__ = 'PhongVu'
import math


class Bar:
    def __init__(self, container_width, container_height, color, position):
        self.dx = math.floor(container_width/10)
        self.dy = math.floor(self.dx/3)

        if self.dy > 25:
            self.dy = 25

        if str.upper(position) == "TOP":
            self.fy = 0
            self.ly = self.fy + self.dy

            self.fx = 0
            self.lx = self.fx + self.dx
        else:
            self.ly = container_height - 1
            self.fy = self.ly - self.dy

            self.lx = container_width - 1
            self.fx = self.lx - self.dx
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
