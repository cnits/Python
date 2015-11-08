# __author__ = 'PhongVu'
# import sys
from Board import *
from Ball import *
from Bar import *

MIN_W = 250
MIN_H = 150

BOARD_COLOR = "#E1E1E1"
BALL_COLOR = "#1E90FF"
BTOP_COLOR = "GREEN"
BBOTTOM_COLOR = "#FF0000"
SPEED = [5, 5]
MIN_DELAY = 1
MAX_DELAY = 30


class BingBall(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.isAuto = True
        self.isPlaying = False
        self.DELAY = int(math.ceil(MAX_DELAY/2))

        self.W = self.parent.winfo_screenwidth() - MIN_W
        self.H = self.parent.winfo_screenheight() - MIN_H
        if self.W < MIN_W:
            self.W = MIN_W
        if self.H < MIN_H:
            self.H = MIN_H

        self.board = Board(self)
        self.ball = Ball(self.board)
        self.barTop = Bar(self.board, 1)
        self.barBottom = Bar(self.board, 3)

        self.initialize()

    def initialize(self):
        self.reset_score()
        self.parent.title("BingBall Game")
        self.parent.config(bg="#324b21")

        self.pack(side=RIGHT, padx=5, pady=5)

    def reset_score(self):
        self.barTop.reset_score()
        self.barBottom.reset_score()
        redTeam.set(str(self.barBottom.score))
        greenTeam.set(str(self.barTop.score))

    def direct_ball(self):
        fx, fy, lx, ly = self.board.coords(self.ball.get_name())
        global top, bottom
        top = bottom = False
        tmp = self.board.find_overlapping(fx, fy, lx, ly)

        if fx <= 0:
            SPEED[0] = math.fabs(SPEED[0])
        if lx >= self.W:
            SPEED[0] = -math.fabs(SPEED[0])
        if fy <= 0 or (len(tmp) > 1 and fy < self.H/2 and ly < self.H):
            SPEED[1] = math.fabs(SPEED[1])
            if fy <= 0:
                top = True
        if ly >= self.H or (len(tmp) > 1 and fy > self.H/2 and ly < self.H):
            SPEED[1] = -math.fabs(SPEED[1])
            if ly >= self.H:
                bottom = True

    def process_move_manual(self):
        if self.isPlaying is False:
            return 1
        global top, bottom
        self.direct_ball()
        # self.direct_bar_auto()
        self.board.move(self.ball.get_name(), SPEED[0], SPEED[1])
        if top is True or bottom is True:
            x1, y1, x2, y2 = self.board.coords(self.ball.get_name())
            tmp = self.board.find_overlapping(x1, y1, x2, y2)
            if len(tmp) <= 1:
                if top is True:
                    self.barBottom.set_score(1)
                    redTeam.set(str(self.barBottom.score))
                else:
                    self.barTop.set_score(1)
                    greenTeam.set(str(self.barTop.score))
        self.board.after(self.DELAY, self.process_move_manual)

    def process_move_auto(self):
        if self.isPlaying is False:
            return 1
        global top, bottom
        self.direct_ball()
        self.direct_bar_auto()
        self.board.move(self.ball.get_name(), SPEED[0], SPEED[1])
        if top is True or bottom is True:
            x1, y1, x2, y2 = self.board.coords(self.ball.get_name())
            tmp = self.board.find_overlapping(x1, y1, x2, y2)
            if len(tmp) <= 1:
                if top is True:
                    self.barBottom.set_score(1)
                    redTeam.set(str(self.barBottom.score))
                else:
                    self.barTop.set_score(1)
                    greenTeam.set(str(self.barTop.score))
        self.board.after(self.DELAY, self.process_move_auto)

    def direct_bar_auto(self):
        fx, fy, lx, ly = self.board.coords(self.ball.get_name())
        if fy + self.H*SPEED[1] <= 0:
            self.move_bar(self.barTop.get_name(), 10 + fx + 2*SPEED[0])
        if ly + self.H*SPEED[1] >= self.H:
            self.move_bar(self.barBottom.get_name(), lx + 2*SPEED[0] - 10)

    def move_bar(self, bar, x):
        x0, y0, x1, y1 = self.board.coords(bar)
        if x < x0:
            self.board.move(bar, x - x0, 0)
        if x > x1:
            self.board.move(bar, x - x1, 0)

    def bar_top_event_left(self, event):
        x0, y0, x1, y1 = self.board.coords(self.barTop.get_name())
        if x0 > 0:
            self.board.move(self.barTop.get_name(), -2*math.fabs(SPEED[0]), 0)

    def bar_top_event_right(self, event):
        x0, y0, x1, y1 = self.board.coords(self.barTop.get_name())
        if x1 < self.W:
            self.board.move(self.barTop.get_name(), 2*math.fabs(SPEED[0]), 0)

    def bar_bottom_event_left(self, event):
        x0, y0, x1, y1 = self.board.coords(self.barBottom.get_name())
        if x0 > 0:
            self.board.move(self.barBottom.get_name(), -2*math.fabs(SPEED[0]), 0)

    def bar_bottom_event_right(self, event):
        x0, y0, x1, y1 = self.board.coords(self.barBottom.get_name())
        if x1 < self.W:
            self.board.move(self.barBottom.get_name(), 2*math.fabs(SPEED[0]), 0)

    def bar_top_event(self, event):
        x0, y0, x1, y1 = self.board.coords(self.barTop.get_name())
        if event.x < x0:
            self.board.move(self.barTop.get_name(), event.x - x0, 0)
        if event.x > x1:
            self.board.move(self.barTop.get_name(), event.x - x1, 0)

    def play_event(self, event):
        if self.isPlaying is True:
            self.isPlaying = False
        else:
            self.isPlaying = True
            self.play()

    def play(self):
        if self.isAuto is True:
            self.process_move_auto()
        else:
            self.process_move_manual()

    def auto_play_event(self, event):
        if self.isPlaying is False:
            self.isAuto = True
            self.reset_score()
            self.reset_event_switch()

    def manual_play_event(self, event):
        if self.isPlaying is False:
            self.isAuto = False
            self.reset_score()
            self.reset_event_switch()

    def up_delay_event(self, event):
        if self.DELAY < MAX_DELAY:
            self.DELAY += 1

    def down_delay_event(self, event):
        if self.DELAY > MIN_DELAY:
            self.DELAY -= 1

    def main(self):
        self.parent.bind("<space>", self.play_event)
        self.parent.bind("<F1>", self.auto_play_event)
        self.parent.bind("<F2>", self.manual_play_event)
        self.parent.bind("<Up>", self.down_delay_event)
        self.parent.bind("<Down>", self.up_delay_event)
        self.reset_event_switch()
        self.play()

    def reset_event_switch(self):
        if self.isAuto is True:
            self.parent.unbind("<Left>")
            self.parent.unbind("<Right>")
            self.board.unbind("<1>")
        else:
            # root.bind("<A>", app.bar_top_event_left)
            # root.bind("<D>", app.bar_top_event_right)
            self.parent.bind("<Left>", self.bar_bottom_event_left)
            self.parent.bind("<Right>", self.bar_bottom_event_right)
            self.board.bind("<1>", self.bar_top_event)


class MainApp:
    def __init__(self):
        self.root = Tk()
        global greenTeam, redTeam
        greenTeam = StringVar()
        redTeam = StringVar()

    def create_widget(self):
        greenTeam.set("0")
        redTeam.set("0")
        Label(self.root, text="G-Team", bd=1, font=("Helvetica", 14),
              fg="#FFFFFF", bg=BTOP_COLOR).pack(side=TOP, padx=5, pady=5)
        Label(self.root, textvariable=greenTeam, bd=1, font=("Helvetica", 20),
              fg="purple", bg=BTOP_COLOR).pack(side=TOP, padx=5, pady=2)

        Label(self.root, text="R-Team", bd=1, font=("Helvetica", 14),
              fg="#FFFFFF", bg=BBOTTOM_COLOR).pack(side=BOTTOM, padx=5, pady=5)
        Label(self.root, textvariable=redTeam, bd=1, font=("Helvetica", 20),
              fg="blue", bg=BBOTTOM_COLOR).pack(side=BOTTOM, padx=5, pady=2)

    def main(self):
        bb = BingBall(self.root)
        # To prevent resizing a frame
        self.root.resizable(False, False)
        try:
            self.create_widget()
            bb.main()
        except IOError as e:
            sys.exit()
        self.root.bind("<Escape>", self.exit_event)
        self.root.geometry(
            "%dx%d+%d+%d" % (bb.W + 120, bb.H + 10, 20, 20)
        )
        self.root.mainloop()

    def exit_event(self, event):
        self.root.destroy()
        sys.exit(0)


if __name__ == "__main__":
    app = MainApp()
    app.main()
