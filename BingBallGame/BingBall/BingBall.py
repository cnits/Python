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
        corner = random.randint(0, 90)
        print(xc, yc)
        #while 1:
        #x2, y2 = i + SPEED, i + SPEED
        #self.board.move("ball", x2-x1, y2-y1)
        #self.board.after(200)
        #self.board.update()

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

