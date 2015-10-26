# __author__ = 'PhongVu'
# import sys
from Board import *
from Ball import *
from Bar import *
from Tkinter import *

WIDTH, HEIGHT = 650, 450
BOARD_COLOR = "#E1E1E1"
BALL_COLOR = "#1E90FF"
BTOP_COLOR = "Green"
BBOTTOM_COLOR = "#FF0000"
SPEED = [5, 5]
DELAY = 2


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

        self.board.bind("<1>", self.bar_top_move)
        self.board.bind("<Right>", self.bar_bottom_move)

    def direct_ball(self):
        fx, fy, lx, ly = self.board.coords("ball")
        if fx <= 0:
            SPEED[0] = math.fabs(SPEED[0])
        if lx >= WIDTH:
            SPEED[0] = -math.fabs(SPEED[0])
        if fy <= 0:
            SPEED[1] = math.fabs(SPEED[1])
        if ly >= HEIGHT:
            SPEED[1] = -math.fabs(SPEED[1])

    def direct_ball_rely_on_bar(self):
        fx, fy, lx, ly = self.board.coords("ball")
        pass

    def process_move(self):
        self.direct_ball()
        self.direct_bar_auto()
        self.board.move("ball", SPEED[0], SPEED[1])
        self.after(DELAY, self.process_move)

    def direct_bar_auto(self):
        fx, fy, lx, ly = self.board.coords("ball")
        if fy + SPEED[1] <= 0:
            self.move_bar("barTop", fx + SPEED[0])
        if ly + SPEED[1] >= HEIGHT:
            self.move_bar("barBottom", lx + SPEED[0])

    def move_bar(self, bar, x):
        x0, y0, x1, y1 = self.board.coords(bar)
        if x < x0:
            self.board.move(bar, x - x0, 0)
        if x > x1:
            self.board.move(bar, x - x1, 0)

    def bar_top_move(self, event):
        x0, y0, x1, y1 = self.board.coords("barTop")
        if event.x < x0:
            self.board.move("barTop", event.x - x0, 0)
        if event.x > x1:
            self.board.move("barTop", event.x - x1, 0)

    def bar_bottom_move(self, event):
        print("TTT")

if __name__ == "__main__":
    root = Tk()
    app = BingBall(root)
    # left = (root.winfo_screenwidth() - WIDTH) / 2
    # top = (root.winfo_screenheight() - HEIGHT) / 2
    # root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, left, top))
    # To prevent resizing a frame
    root.resizable(0, 0)
    try:
        app.process_move()
    except IOError, e:
        print e
        sys.exit()
    root.mainloop()
