# __author__ = 'PhongVu'
import math
import random
import BBConfig as bbc


class Ball:
    def __init__(self, board):
        self.board = board
        _width = self.board.winfo_reqwidth()
        _height = self.board.winfo_reqheight()

        temp = _height
        if _width < _height:
            temp = _width
        self.d = math.floor(temp/10)

        self.fx = random.randint(0, _width - 2*self.d)
        self.fy = random.randint(0, _height - 2*self.d)
        self.lx = self.fx + self.d
        self.ly = self.fy + self.d
        self.color = bbc.BALL_COLOR
        self.touched = -1

        self.setup_ball()

    def setup_ball(self):
        self.board.create_oval(
            self.get_coords(),
            outline="red", fill=self.get_color(),
            width=1, tags=self.get_name()
        )
        self.board.set_ball_name(self.get_name())

    def set_coords(self, fx, fy, lx, ly):
        self.fx, self.fy, self.lx, self.ly = fx, fy, lx, ly

    def set_color(self, color):
        self.color = color

    def get_coords(self):
        return self.fx, self.fy, self.lx, self.ly

    def get_current_coords(self):
        return self.board.coords(self.get_name())

    def get_color(self):
        return self.color

    @staticmethod
    def get_name():
        return "ball"

    def direct_v_ball(self):
        fx, fy, lx, ly = self.get_current_coords()
        tmp = self.board.find_overlapping(fx, fy, lx, ly)
        self.touched = -1
        if fx <= 0:
            bbc.SPEED[0] = math.fabs(bbc.SPEED[0])
        if lx >= self.board.winfo_reqwidth():
            bbc.SPEED[0] = -math.fabs(bbc.SPEED[0])
        if fy <= 0 or \
                (len(tmp) > 1 and ly < self.board.winfo_reqheight()/2 and fy > 0):
            bbc.SPEED[1] = math.fabs(bbc.SPEED[1])
            if fy <= 0:
                self.touched = bbc.BAR_T
        if ly >= self.board.winfo_reqheight() or \
                (len(tmp) > 1 and fy > self.board.winfo_reqheight()/2 and ly < self.board.winfo_reqheight()):
            bbc.SPEED[1] = -math.fabs(bbc.SPEED[1])
            if ly >= self.board.winfo_reqheight():
                self.touched = bbc.BAR_B

    def direct_h_ball(self):
        fx, fy, lx, ly = self.get_current_coords()
        tmp = self.board.find_overlapping(fx, fy, lx, ly)
        self.touched = -1
        if fy <= 0:
            bbc.SPEED[1] = math.fabs(bbc.SPEED[1])
        if ly >= self.board.winfo_reqheight():
            bbc.SPEED[1] = -math.fabs(bbc.SPEED[1])
        if fx <= 0 or \
                (len(tmp) > 1 and lx < self.board.winfo_reqwidth()/2 and fx > 0):
            bbc.SPEED[0] = math.fabs(bbc.SPEED[0])
            if fy <= 0:
                self.touched = bbc.BAR_L
        if lx >= self.board.winfo_reqwidth() or \
                (len(tmp) > 1 and fx > self.board.winfo_reqwidth()/2 and lx < self.board.winfo_reqwidth()):
            bbc.SPEED[0] = -math.fabs(bbc.SPEED[0])
            if ly >= self.board.winfo_reqwidth():
                self.touched = bbc.BAR_R

    def do_moving(self):
        if bbc.IS_PLAYING is False:
            return 1
        bar_pos = self.board.get_bar_pos()
        if bar_pos == bbc.BAR_T or bar_pos == bbc.BAR_B:
            self.direct_v_ball()
        else:
            self.direct_h_ball()
        self.board.move(self.get_name(), bbc.SPEED[0], bbc.SPEED[1])
        self.board.after(bbc.DELAY, self.do_moving)
        if self.touched in [bbc.BAR_T, bbc.BAR_B, bbc.BAR_L, bbc.BAR_R]:
            x1, y1, x2, y2 = self.get_current_coords()
            tmp = self.board.find_overlapping(x1, y1, x2, y2)
            if len(tmp) <= 1:
                if self.touched in [bbc.BAR_T, bbc.BAR_L]:
                    # R won - G failed
                    bbc.BAR_SCORE_R += 1
                else:
                    if self.touched in [bbc.BAR_B, bbc.BAR_R]:
                        # G won - R failed
                        bbc.BAR_SCORE_G += 1
