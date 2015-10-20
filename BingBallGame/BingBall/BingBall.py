# __author__ = 'PhongVu'
# import sys
import random
# import math
from Board import *
from Ball import *
from Bar import *
from Tkinter import *

WIDTH, HEIGHT = 650, 450
BOARD_COLOR = "#E1E1E1"
BALL_COLOR = "#1E90FF"
BTOP_COLOR = "Green"
BBOTTOM_COLOR = "#FF0000"
SPEED = 300


class BingBall(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.board = Board(self, WIDTH, HEIGHT, BOARD_COLOR)
        self.ball = Ball(WIDTH, HEIGHT, BALL_COLOR)

        self.delta = self.ball.d/2
        self.delta_bar = self.ball.d

        self.barTop = Bar(WIDTH, HEIGHT, BTOP_COLOR, "TOP")
        self.barBottom = Bar(WIDTH, HEIGHT, BBOTTOM_COLOR, "BOTTOM")

        self.initialize()

    def initialize(self):
        self.parent.title("BingBall Game")
        self.parent.config(bg="#324b21")

        self.board.create_oval(
            self.ball.get_coord(),
            outline="red", fill=self.ball.get_color(),
            width=1, tags="ball"
        )

        self.board.create_rectangle(
            self.barTop.get_coord(),
            outline="#05f", fill=self.barTop.get_color(),
            width=1, tags="barTop"
        )

        self.board.create_rectangle(
            self.barBottom.get_coord(),
            outline="#05f", fill=self.barBottom.get_color(),
            tags="barBottom"
        )

        self.board.pack(fill=BOTH, expand=1)
        self.pack(fill=X, padx=5, pady=5)

    def process_move(self):
        ball = self.board.find_withtag("ball")
        xc1, yc1, xc2, yc2 = self.board.coords(ball)
        xc, yc = self.get_average_coord(xc1, yc1, xc2, yc2)

        xi, yi = self.random_position()
        if xi == xc:
            if yi == yc:
                self.move_to_right(xc=xc, yc=yc)
            elif yi < yc:
                self.move_to_top(xc=xc, yc=yc)
            else:
                self.move_to_bottom(xc=xc, yc=yc)
        elif xc < xc:
            if yi == yc:
                self.move_to_left(xc=xc, yc=yc)
            elif yi < yc:
                self.move_left_top(xc=xc, yc=yc)
            else:
                self.move_left_bottom(xc=xc, yc=yc)
        else:
            if yi == yc:
                self.move_to_right(xc=xc, yc=yc)
            elif yi < yc:
                self.move_right_top(xc=xc, yc=yc)
            else:
                self.move_right_bottom(xc=xc, yc=yc)

    def move_right_top(self, xc, yc):
        corner = random.randint(0, 90)
        if corner == 0:
            self.move_to_top(xc=xc, yc=yc)
        elif corner == 90:
            self.move_to_right(xc=xc, yc=yc)
        else:
            k = yc
            d = math.floor(k*math.tan(math.radians(corner)))
            if xc + d > WIDTH:
                corner = 90 - corner
                k = WIDTH - xc
                d = math.floor(k*math.tan(math.radians(corner)))
                xi, yi = WIDTH - self.delta, yc - d
                self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
                self.move_left_top(xc=xi, yc=yi)
            else:
                xi, yi = xc + d, 0 + self.delta
                self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
                self.move_right_bottom(xc=xi, yc=yi)

    def move_right_bottom(self, xc, yc):
        corner = random.randint(10, 80)
        if corner == 0:
            self.move_to_bottom(xc=xc, yc=yc)
        elif corner == 90:
            self.move_to_right(xc=xc, yc=yc)
        else:
            k = HEIGHT - yc
            d = math.floor(k*math.tan(math.radians(corner)))
            if xc + d > WIDTH:
                corner = 90 - corner
                k = WIDTH - xc
                d = math.floor(k*math.tan(math.radians(corner)))
                xi, yi = WIDTH - self.delta, HEIGHT - yc - d
                self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
                self.move_left_bottom(xc=xi, yc=yi)
            else:
                xi, yi = xc + d, HEIGHT - self.delta
                self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
                self.move_right_top(xc=xi, yc=yi)

    def move_left_top(self, xc, yc):
        corner = random.randint(10, 80)
        if corner == 0:
            self.move_to_top(xc=xc, yc=yc)
        elif corner == 90:
            self.move_to_left(xc=xc, yc=yc)
        else:
            k = yc
            d = math.floor(k*math.tan(math.radians(corner)))
            if xc - d < 0:
                corner = 90 - corner
                k = xc
                d = math.floor(k*math.tan(math.radians(corner)))
                xi, yi = 0 + self.delta, yc - d
                self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
                self.move_right_top(xc=xi, yc=yi)
            else:
                xi, yi = xc - d, 0 + self.delta
                self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
                self.move_left_bottom(xc=xi, yc=yi)

    def move_left_bottom(self, xc, yc):
        corner = random.randint(10, 80)
        if corner == 0:
            self.move_to_bottom(xc=xc, yc=yc)
        elif corner == 90:
            self.move_to_left(xc=xc, yc=yc)
        else:
            k = HEIGHT - yc
            d = math.floor(k*math.tan(math.radians(corner)))
            if xc - d < 0:
                corner = 90 - corner
                k = xc
                d = math.floor(k*math.tan(math.radians(corner)))
                xi, yi = 0 + self.delta, HEIGHT - yc - d
                self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
                self.move_right_bottom(xc=xi, yc=yi)
            else:
                xi, yi = xc - d, HEIGHT - self.delta
                self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
                self.move_left_top(xc=xi, yc=yi)

    def move_to_right(self, xc, yc):
        xi, yi = WIDTH - self.delta, yc
        self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
        bit = random.getrandbits(1)
        if bit == 1:
            self.move_left_top(xc=xi, yc=yi)
        else:
            self.move_left_bottom(xc=xi, yc=yi)

    def move_to_left(self, xc, yc):
        xi, yi = 0 + self.delta, yc
        self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
        bit = random.getrandbits(1)
        if bit == 1:
            self.move_right_top(xc=xi, yc=yi)
        else:
            self.move_right_bottom(xc=xi, yc=yi)

    def move_to_top(self, xc, yc):
        xi, yi = xc, 0 + self.delta
        self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
        bit = random.getrandbits(1)
        if bit == 1:
            self.move_right_bottom(xc=xi, yc=yi)
        else:
            self.move_left_bottom(xc=xi, yc=yi)

    def move_to_bottom(self, xc, yc):
        xi, yi = xc, HEIGHT - self.delta
        self.todo_move(xc=xc, yc=yc, xi=xi, yi=yi)
        bit = random.getrandbits(1)
        if bit == 1:
            self.move_right_top(xc=xi, yc=yi)
        else:
            self.move_left_top(xc=xi, yc=yi)

    @classmethod
    def random_position(cls):
        return random.randint(0, WIDTH), random.randint(0, HEIGHT)

    @classmethod
    def get_average_coord(cls, x0, y0, x1, y1):
        return int((x0+x1)/2), int((y0+y1)/2)

    def todo_move(self, xc, yc, xi, yi):
        self.board.move("ball", xi-xc, yi-yc)
        self.board.after(100)
        self.board.update()

if __name__ == "__main__":
    root = Tk()
    app = BingBall(root)
    # root.geometry("650x450+300+300")
    # To prevent resizing a frame
    root.resizable(0, 0)
    try:
        app.process_move()
    except IOError, e:
        print e
        sys.exit(1)
    root.mainloop()
