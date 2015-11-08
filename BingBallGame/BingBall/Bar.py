# __author__ = 'PhongVu'
import math
import BBConfig as bbc


class Bar:
    def __init__(self, board, position):
        self.board = board
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
            self.color = bbc.BAR_COLOR_1
            if self.position == bbc.BAR_T:
                self.set_coord(0, 0, self.dx, self.dy)
            else:
                self.set_coord(0, 0, self.dy, self.dx)
        else:
            self.color = bbc.BAR_COLOR_2
            if self.position == bbc.BAR_B:
                self.set_coord(
                    self.board.winfo_reqwidth() - 1 - self.dx,
                    self.board.winfo_reqheight() - 1 - self.dy,
                    self.board.winfo_reqwidth() - 1,
                    self.board.winfo_reqheight() - 1
                )
            else:
                self.set_coord(
                    self.board.winfo_reqwidth() - 1 - self.dy,
                    self.board.winfo_reqheight() - 1 - self.dx,
                    self.board.winfo_reqwidth() - 1,
                    self.board.winfo_reqheight() - 1
                )
        self.board.create_rectangle(
            self.get_coord(),
            outline="#05f", fill=self.get_color(),
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

    def set_score(self, score):
        if isinstance(score, int) is False:
            score = 1
        self.score += score

    def reset_score(self):
        self.score = 0

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
            name = "bar"
        return name
