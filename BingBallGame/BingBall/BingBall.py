# __author__ = 'PhongVu'
# import sys
from Board import *
from Ball import *
from Bar import *
try:
    from Tkinter import *
except IOError, e:
    from tkinter import *

WIDTH, HEIGHT = 650, 450
BOARD_COLOR = "#E1E1E1"
BALL_COLOR = "#1E90FF"
BTOP_COLOR = "GREEN"
BBOTTOM_COLOR = "#FF0000"
SPEED = [8, 8]
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
        global g, r
        g = r = 0
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
        self.pack(side=RIGHT, padx=5, pady=5)

        # self.board.bind("<1>", self.bar_top_event())
        # self.board.bind("<Right>", self.bar_bottom_event())

    def direct_ball(self):
        fx, fy, lx, ly = self.board.coords("ball")
        global top, bottom
        top = bottom = False
        if fx <= 0:
            SPEED[0] = math.fabs(SPEED[0])
        if lx >= WIDTH:
            SPEED[0] = -math.fabs(SPEED[0])
        if fy <= 0:
            SPEED[1] = math.fabs(SPEED[1])
            top = True
        if ly >= HEIGHT:
            SPEED[1] = -math.fabs(SPEED[1])
            bottom = True

    def direct_ball_rely_on_bar(self):
        fx, fy, lx, ly = self.board.coords("ball")
        pass

    def process_move(self):
        global top, bottom, g, r
        self.direct_ball()
        self.direct_bar_auto()
        self.board.move("ball", SPEED[0], SPEED[1])
        if top is True or bottom is True:
            x1, y1, x2, y2 = self.board.coords("ball")
            tmp = self.board.find_overlapping(x1, y1, x2, y2)
            if len(tmp) <= 1:
                if top is True:
                    r += 1
                    redTeam.set(str(r))
                else:
                    g += 1
                    greenTeam.set(str(g))
        self.after(DELAY, self.process_move)

    def direct_bar_auto(self):
        fx, fy, lx, ly = self.board.coords("ball")
        if fy + HEIGHT*SPEED[1] <= 0:
            self.move_bar("barTop", 10 + fx + 2*SPEED[0])
        if ly + HEIGHT*SPEED[1] >= HEIGHT:
            self.move_bar("barBottom", lx + 2*SPEED[0] - 10)

    def move_bar(self, bar, x):
        x0, y0, x1, y1 = self.board.coords(bar)
        if x < x0:
            self.board.move(bar, x - x0, 0)
        if x > x1:
            self.board.move(bar, x - x1, 0)

    def bar_top_event(self, event):
        x0, y0, x1, y1 = self.board.coords("barTop")
        if event.x < x0:
            self.board.move("barTop", event.x - x0, 0)
        if event.x > x1:
            self.board.move("barTop", event.x - x1, 0)

    def bar_bottom_event(self, event):
        pass

    @classmethod
    def create_widget(cls, master):
        global greenTeam, redTeam
        greenTeam = StringVar()
        redTeam = StringVar()
        greenTeam.set("0")
        redTeam.set("0")
        Label(master, text="G-Team", bd=1, font=("Helvetica", 16),
              fg="#FFFFFF", bg=BTOP_COLOR).pack(side=TOP, padx=5, pady=5)
        Label(master, textvariable=greenTeam, bd=1, font=("Helvetica", 20),
              fg="purple", bg=BTOP_COLOR).pack(side=TOP, padx=5, pady=2)

        Label(master, text="R-Team", bd=1, font=("Helvetica", 16),
              fg="#FFFFFF", bg=BBOTTOM_COLOR).pack(side=BOTTOM, padx=5, pady=5)
        Label(master, textvariable=redTeam, bd=1, font=("Helvetica", 20),
              fg="blue", bg=BBOTTOM_COLOR).pack(side=BOTTOM, padx=5, pady=2)

if __name__ == "__main__":
    root = Tk()
    app = BingBall(root)
    # To prevent resizing a frame
    root.resizable(False, False)
    try:
        app.create_widget(root)
        app.process_move()
    except IOError, e:
        print e
        sys.exit()
    root.mainloop()
