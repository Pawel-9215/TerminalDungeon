import curses
from math import floor

class button():
    is_focused = False
    state = {True:2, False:1}
    content = ""
    pos_y = 0
    pos_x = 0
    window = None
    
    def __init__(self, window, pos_y, pos_x, content, name):

        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.window = window
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.content = content

    def toggle(self):
        self.is_focused = not self.is_focused

class Label():
    content = ""
    def __init__(self, window, content, pos_y, pos_x):
        self.content = content
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.window = window

    def draw(self):
        self.window.addstr(self.pos_y, self.pos_x, self.content)


def popup(mess, wholescr_y, wholescr_x):
    width = len(mess)+4
    height = 3

    popup = curses.newwin(height, width, floor(wholescr_y/2)-2, floor(wholescr_x/2)-floor(width/2))
    popup.border()
    popup.addstr(1, 2, mess)
    popup.refresh()