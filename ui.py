import curses
from math import floor


class button():
    is_focused = False
    state = {True: 2, False: 1}
    content = ""
    pos_y = 0
    pos_x = 0
    window = None
    func = None
    arguments = []

    def __init__(self, window, pos_y, pos_x, content, name, on_pressed, arguments):

        self.window = window
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.content = content
        self.colors = ColorInit()
        self.name = name
        self.func = on_pressed
        self.arguments = arguments

    def toggle(self):
        self.is_focused = not self.is_focused

    def draw(self):
        if self.is_focused:
            self.window.addstr(self.pos_y, self.pos_x, self.content, curses.A_STANDOUT)
        else:
            self.window.addstr(self.pos_y, self.pos_x, self.content,
                               curses.color_pair(self.colors.font_color["magenta"]))

    def on_pressed(self):
        self.func(*self.arguments)


class Label():

    def __init__(self, window, content, pos_y, pos_x, bg="white"):
        self.content = content
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.window = window
        self.colors = ColorInit()
        self.bg = bg

    def draw(self):
        self.window.addstr(self.pos_y, self.pos_x, self.content, curses.color_pair(self.colors.bg_color[self.bg]))


class Plain_text():

    def __init__(self, window, content, pos_y, pos_x):
        self.content = content
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.window = window

    def draw(self):
        self.window.addstr(self.pos_y, self.pos_x, self.content)


class ColorInit():
    font_color = {
        "yellow": 1,
        "blue": 3,
        "red": 4,
        "magenta": 5,
    }
    bg_color = {
        "white": 21,
        "yellow": 22,
        "magenta": 23
    }

    def __init__(self):
        # font colors
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)

        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

        # bg colors
        curses.init_pair(21, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(22, curses.COLOR_BLACK, curses.COLOR_BLUE)
        curses.init_pair(23, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
        curses.init_pair(24, curses.COLOR_BLACK, curses.COLOR_RED)


class Rotator():

    def __init__(self, window, items: list, y, x):
        self.items = items
        self.choosen_item = 0
        self.y = y
        self.x = x
        self.window = window

    def draw(self):
        if len(self.items) <= 1:
            self.window.addstr(self.y + 1, self.x, ">" + self.items[self.choosen_item], curses.A_STANDOUT)
        else:
            for i in range(3):
                if i == 1:
                    self.window.addstr(self.y + i, self.x, ">" + self.items[self.choosen_item - 1 + i] + " " * (
                                16 - len(self.items[self.choosen_item])), curses.A_STANDOUT)
                elif self.choosen_item - 1 + i >= len(self.items):
                    self.window.addstr(self.y + i, self.x, " " + self.items[0])
                else:
                    self.window.addstr(self.y + i, self.x, " " + self.items[self.choosen_item - 1 + i])

    def rotate(self, direction: int):
        if self.choosen_item + direction >= len(self.items):
            self.choosen_item = 0
        elif self.choosen_item + direction < 0:
            self.choosen_item = len(self.items) - 1
        else:
            self.choosen_item = self.choosen_item + direction

    def get_chosen_item(self):
        return self.items[self.choosen_item]


def popup(mess, wholescr_y, wholescr_x):
    width = len(mess) + 4
    height = 3

    popup = curses.newwin(height, width, floor(wholescr_y / 2) - 2, floor(wholescr_x / 2) - floor(width / 2))
    popup.border()
    popup.addstr(1, 2, mess)
    popup.refresh()
