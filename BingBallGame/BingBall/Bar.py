# __author__ = 'PhongVu'
import math
import BBConfig as bbc


class Bar:
    def __init__(self, board, position):
        self.board = board
        self.board.put_bar_pos(position)
        self.dx = math.floor(board.winfo_reqwidth()/10)
        self.dy = math.floor(self.dx/3)
        if self.dy > 25:
            self.dy = 25

        self.fy, self.ly, self.fx, self.lx = 0, 0, 0, 0
        self.color = ""
        self.position = position
        self.score = 0
        self.setup_bar()

    def setup_bar(self):
        if self.position == bbc.BAR_T or self.position == bbc.BAR_L:
            self.color = bbc.BAR_COLOR_G
            self.board.set_bar_g_name(self.get_name())
            if self.position == bbc.BAR_T:
                self.set_coords(0, 0, self.dx, self.dy)
            else:
                self.set_coords(0, 0, self.dy, self.dx)
        else:
            self.color = bbc.BAR_COLOR_R
            self.board.set_bar_r_name(self.get_name())
            if self.position == bbc.BAR_B:
                self.set_coords(
                    self.board.winfo_reqwidth() - 1 - self.dx,
                    self.board.winfo_reqheight() - 1 - self.dy,
                    self.board.winfo_reqwidth() - 1,
                    self.board.winfo_reqheight() - 1
                )
            else:
                self.set_coords(
                    self.board.winfo_reqwidth() - 1 - self.dy,
                    self.board.winfo_reqheight() - 1 - self.dx,
                    self.board.winfo_reqwidth() - 1,
                    self.board.winfo_reqheight() - 1
                )
        self.board.create_rectangle(
            self.get_coords(),
            outline="#05f", fill=self.get_color(),
            width=1, tags=self.get_name()
        )

    def set_coords(self, fx, fy, lx, ly):
        self.fx, self.fy, self.lx, self.ly = fx, fy, lx, ly

    def set_color(self, color):
        self.color = color

    def get_coords(self):
        return self.fx, self.fy, self.lx, self.ly

    def get_color(self):
        return self.color

    def get_name(self):
        if self.position == bbc.BAR_T:
            name = "barT"
        elif self.position == bbc.BAR_B:
            name = "barB"
        elif self.position == bbc.BAR_L:
            name = "barL"
        elif self.position == bbc.BAR_R:
            name = "barR"
        else:
            name = None
        return name

    def do_moving(self, axis):
        x0, y0, x1, y1 = self.board.coords(self.get_name())
        delta_x, delta_y = 0, 0
        if self.position == bbc.BAR_T or self.position == bbc.BAR_B:
            if axis < x0:
                delta_x = axis - x0
            if axis > x1:
                delta_x = axis - x1
        else:
            if axis < y0:
                delta_y = axis - y0
            if axis > y1:
                delta_y = axis - y1
        self.board.move(self.get_name(), delta_x, delta_y)