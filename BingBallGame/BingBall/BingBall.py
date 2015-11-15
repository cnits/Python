# __author__ = 'PhongVu'
# import sys
from Board import *
from Ball import *
from Bar import *
import BBConfig as bbc

MIN_DELAY = 1
MAX_DELAY = 30


class BingBall(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.DELAY = int(math.ceil(MAX_DELAY/2))

        self.W = self.parent.winfo_screenwidth() - bbc.MIN_W
        self.H = self.parent.winfo_screenheight() - bbc.MIN_H
        if self.W < bbc.MIN_W:
            self.W = bbc.MIN_W
        if self.H < bbc.MIN_H:
            self.H = bbc.MIN_H

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
        bbc.BAR_SCORE_G = 0
        bbc.BAR_SCORE_R = 0

    def process_move_manual(self):
        self.ball.do_moving()

    def process_move_auto(self):
        if bbc.IS_PLAYING is False:
            return 1
        self.ball.direct_v_ball()
        self.direct_bar_auto()
        self.board.move(self.ball.get_name(), bbc.SPEED[0], bbc.SPEED[1])
        if self.ball.touched in [bbc.BAR_T, bbc.BAR_B, bbc.BAR_L, bbc.BAR_R]:
            x1, y1, x2, y2 = self.ball.get_current_coords()
            tmp = self.board.find_overlapping(x1, y1, x2, y2)
            if len(tmp) <= 1:
                if self.ball.touched in [bbc.BAR_T, bbc.BAR_L]:
                    # R won - G failed
                    bbc.BAR_SCORE_R += 1
                else:
                    if self.ball.touched in [bbc.BAR_B, bbc.BAR_R]:
                        # G won - R failed
                        bbc.BAR_SCORE_G += 1
        self.board.after(self.DELAY, self.process_move_auto)

    def direct_bar_auto(self):
        fx, fy, lx, ly = self.board.coords(self.ball.get_name())
        if fy + self.H*bbc.SPEED[1] <= 0:
            self.barTop.do_moving(10 + fx + 2*bbc.SPEED[0])
        if ly + self.H*bbc.SPEED[1] >= self.H:
            self.barBottom.do_moving(lx + 2*bbc.SPEED[0] - 10)

    def bar_top_event_left(self, event):
        x0, y0, x1, y1 = self.board.coords(self.barTop.get_name())
        if x0 > 0:
            self.board.move(self.barTop.get_name(), -2*math.fabs(bbc.SPEED[0]), 0)

    def bar_top_event_right(self, event):
        x0, y0, x1, y1 = self.board.coords(self.barTop.get_name())
        if x1 < self.W:
            self.board.move(self.barTop.get_name(), 2*math.fabs(bbc.SPEED[0]), 0)

    def bar_bottom_event_left(self, event):
        x0, y0, x1, y1 = self.board.coords(self.barBottom.get_name())
        if x0 > 0:
            self.board.move(self.barBottom.get_name(), -2*math.fabs(bbc.SPEED[0]), 0)

    def bar_bottom_event_right(self, event):
        x0, y0, x1, y1 = self.board.coords(self.barBottom.get_name())
        if x1 < self.W:
            self.board.move(self.barBottom.get_name(), 2*math.fabs(bbc.SPEED[0]), 0)

    def bar_top_event(self, event):
        self.barTop.do_moving(event.x)

    def play_event(self, event):
        if bbc.IS_PLAYING is True:
            bbc.IS_PLAYING = False
        else:
            bbc.IS_PLAYING = True
            self.play()

    def play(self):
        if bbc.IS_AUTO is True:
            self.process_move_auto()
        else:
            self.process_move_manual()

    def auto_play_event(self, event):
        if bbc.IS_PLAYING is False:
            bbc.IS_AUTO = True
            self.reset_score()
            self.reset_event_switch()

    def manual_play_event(self, event):
        if bbc.IS_PLAYING is False:
            bbc.IS_AUTO = False
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
        if bbc.IS_AUTO is True:
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
              fg="#FFFFFF", bg=bbc.BAR_COLOR_G).pack(side=TOP, padx=5, pady=5)
        Label(self.root, textvariable=greenTeam, bd=1, font=("Helvetica", 20),
              fg="purple", bg=bbc.BAR_COLOR_G).pack(side=TOP, padx=5, pady=2)

        Label(self.root, text="R-Team", bd=1, font=("Helvetica", 14),
              fg="#FFFFFF", bg=bbc.BAR_COLOR_R).pack(side=BOTTOM, padx=5, pady=5)
        Label(self.root, textvariable=redTeam, bd=1, font=("Helvetica", 20),
              fg="blue", bg=bbc.BAR_COLOR_R).pack(side=BOTTOM, padx=5, pady=2)

    def update_scores(self):
        redTeam.set(str(bbc.BAR_SCORE_R))
        greenTeam.set(str(bbc.BAR_SCORE_G))
        self.root.after(bbc.DELAY, self.update_scores)

    def main(self):
        bb = BingBall(self.root)
        # To prevent resizing a frame
        self.root.resizable(False, False)
        try:
            self.create_widget()
            self.update_scores()
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
