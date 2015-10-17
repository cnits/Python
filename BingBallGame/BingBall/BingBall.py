# __author__ = 'PhongVu'
import sys
import random
import math
from Board import *
from Ball import *
from Tkinter import *

WIDTH, HEIGHT = 650, 450
BOARD_COLOR = "#E1E1E1"
BALL_COLOR = "#1E90FF"
SPEED = 300


class BingBall(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.board = Board(self, WIDTH, HEIGHT, BOARD_COLOR)
        self.ball = Ball(WIDTH, HEIGHT, BALL_COLOR)

        self.initialize()
        self.todo_move()

    def initialize(self):
        self.parent.title("BingBall Game")
        self.parent.config(bg="#324b21")

        self.board.create_oval(
            self.ball.get_coord(),
            outline="red", fill=self.ball.get_color(),
            width=1, tags="ball"
        )

        self.board.pack(fill=BOTH, expand=1)
        self.pack(fill=X, padx=5, pady=5)

    def todo_move(self):
        ball = self.board.find_withtag("ball")
        xc1, yc1, xc2, yc2 = self.board.coords(ball)
        xc, yc = self.get_average_coord(xc1, yc1, xc2, yc2)
        corner = random.randint(1, 90)
        # print(xc, yc)
        xi, yi = self.random_position()
        # print(xi, yi)
        # print(math.tan(math.radians(corner)))
        while 1:
            if xi == xc:
                if yi == yc:
                    xi, yi = self.random_position()
                elif yi < yc:
                    self.move_to_top()
                else:
                    self.move_to_bottom()
            elif xc < xc:
                if yi == yc:
                    self.move_to_left()
                elif yi < yc:
                    self.move_left_top()
                else:
                    self.move_left_bottom()
            else:
                if yi == yc:
                    self.move_to_right()
                elif yi < yc:
                    self.move_right_top()
                else:
                    self.move_right_bottom()
            xc, yc = xi, yi
        # x2, y2 = i + SPEED, i + SPEED
        # self.board.move("ball", x2-x1, y2-y1)
        # self.board.after(200)
        # self.board.update()

    def move_right_top(self):
        pass

    def move_right_bottom(self):
        pass

    def move_to_right(self):
        pass

    def move_left_top(self):
        pass

    def move_left_bottom(self):
        pass

    def move_to_left(self):
        pass

    def move_to_top(self):
        pass

    def move_to_bottom(self):
        pass

    @classmethod
    def random_position(cls):
        return random.randint(0, WIDTH), random.randint(0, HEIGHT)

    @classmethod
    def get_average_coord(cls, x0, y0, x1, y1):
        return int((x0+x1)/2), int((y0+y1)/2)

if __name__ == "__main__":
    root = Tk()
    app = BingBall(root)
    # root.geometry("650x450+300+300")
    # To prevent resizing a frame
    root.resizable(0, 0)
    root.mainloop()

