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

    def get_current_coords(self):
        return self.board.coords(self.get_name())

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

    # M-2-M
    def do_moving(self, axis_of_ball):
        x0, y0, x1, y1 = self.get_current_coords()
        delta_x, delta_y = 0, 0
        if self.position == bbc.BAR_T or self.position == bbc.BAR_B:
            if axis_of_ball < x0:
                delta_x = axis_of_ball - x0
            if axis_of_ball > x1:
                delta_x = axis_of_ball - x1
        else:
            if axis_of_ball < y0:
                delta_y = axis_of_ball - y0
            if axis_of_ball > y1:
                delta_y = axis_of_ball - y1
        self.board.move(self.get_name(), delta_x, delta_y)

    # P-2-P
    def to_move(self, direction):
        x0, y0, x1, y1 = self.get_current_coords()
        delta_x, delta_y = 0, 0
        if direction == bbc.DIRECT_TO_LEFT:
            if self.position in [bbc.BAR_T, bbc.BAR_B]:
                if x0 > 0:
                    delta_x = (-2) * math.fabs(bbc.SPEED[0])
            else:
                if self.position in [bbc.BAR_L, bbc.BAR_R]:
                    if y0 > 0:
                        delta_y = (-2) * math.fabs(bbc.SPEED[1])
        else:
            if direction == bbc.DIRECT_TO_RIGHT:
                if self.position in [bbc.BAR_T, bbc.BAR_B]:
                    if x1 < self.board.winfo_reqwidth():
                        delta_x = 2 * math.fabs(bbc.SPEED[0])
                else:
                    if self.position in [bbc.BAR_L, bbc.BAR_R]:
                        if y1 < self.board.winfo_reqheight():
                            delta_y = 2 * math.fabs(bbc.SPEED[1])
        self.board.move(self.get_name(), delta_x, delta_y)
