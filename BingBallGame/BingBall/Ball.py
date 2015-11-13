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
        self.current = 10

        self.setup_ball()

    def setup_ball(self):
        self.board.create_oval(
            self.get_coord(),
            outline="red", fill=self.get_color(),
            width=1, tags=self.get_name()
        )

    def set_coord(self, fx, fy, lx, ly):
        self.fx, self.fy, self.lx, self.ly = fx, fy, lx, ly

    def set_color(self, color):
        self.color = color

    def get_coord(self):
        return self.fx, self.fy, self.lx, self.ly

    def get_color(self):
        return self.color

    @staticmethod
    def get_name():
        return "ball"

    def direct_v_ball(self):
        fx, fy, lx, ly = self.board.coords(self.get_name())
        tmp = self.board.find_overlapping(fx, fy, lx, ly)

        if fx <= 0:
            bbc.SPEED[0] = math.fabs(bbc.SPEED[0])
        if lx >= self.board.winfo_reqwidth():
            bbc.SPEED[0] = -math.fabs(bbc.SPEED[0])
        if fy <= 0 or \
                (len(tmp) > 1 and ly < self.board.winfo_reqheight()/2 and fy > 0):
            bbc.SPEED[1] = math.fabs(bbc.SPEED[1])
            if fy <= 0:
                self.current = bbc.BAR_T
        if ly >= self.board.winfo_reqheight() or \
                (len(tmp) > 1 and fy > self.board.winfo_reqheight()/2 and ly < self.board.winfo_reqheight()):
            bbc.SPEED[1] = -math.fabs(bbc.SPEED[1])
            if ly >= self.board.winfo_reqheight():
                self.current = bbc.BAR_B

    def direct_h_ball(self):
        fx, fy, lx, ly = self.board.coords(self.get_name())
        tmp = self.board.find_overlapping(fx, fy, lx, ly)

        if fy <= 0:
            bbc.SPEED[1] = math.fabs(bbc.SPEED[1])
        if ly >= self.board.winfo_reqheight():
            bbc.SPEED[1] = -math.fabs(bbc.SPEED[1])
        if fx <= 0 or \
                (len(tmp) > 1 and lx < self.board.winfo_reqwidth()/2 and fx > 0):
            bbc.SPEED[0] = math.fabs(bbc.SPEED[0])
            if fy <= 0:
                self.current = bbc.BAR_L
        if lx >= self.board.winfo_reqwidth() or \
                (len(tmp) > 1 and fx > self.board.winfo_reqwidth()/2 and lx < self.board.winfo_reqwidth()):
            bbc.SPEED[0] = -math.fabs(bbc.SPEED[0])
            if ly >= self.board.winfo_reqwidth():
                self.current = bbc.BAR_R
