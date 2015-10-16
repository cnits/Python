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
D_BALL = WIDTH/10
X0Y0_BALL = math.floor(math.sqrt(math.pow(WIDTH, 2) + math.pow(HEIGHT, 2))/2) - 200
X1Y1_BALL = X0Y0_BALL + D_BALL


class BingBall(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.board = Board(self, WIDTH, HEIGHT, BOARD_COLOR)
        self.ball = self.board.create_oval(
            X0Y0_BALL, X0Y0_BALL, X1Y1_BALL, X1Y1_BALL,
            outline="red", fill=BALL_COLOR,
            width=1, tags="ball"
        )

        self.initialize()
        self.todo_move()

    def initialize(self):
        self.parent.title("BingBall Game")
        self.parent.config(bg="#324b21")

        self.board.pack(fill=BOTH, expand=1)
        self.pack(fill=X, padx=5, pady=5)

    def todo_move(self):
        ball = self.board.find_withtag("ball")
        x1, y1, x2, y2 = self.board.coords("ball")
        x1 = int(x1)
        y1 = int(y1)
        #while 1:
        #x2, y2 = i + SPEED, i + SPEED
        #self.board.move("ball", x2-x1, y2-y1)
        #self.board.after(200)
        #self.board.update()

        print(self.board.bbox(ball))

if __name__ == "__main__":
    root = Tk()
    app = BingBall(root)
    # root.geometry("650x450+300+300")
    # To prevent resizing a frame
    root.resizable(0, 0)
    root.mainloop()

