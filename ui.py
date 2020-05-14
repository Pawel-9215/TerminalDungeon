import curses

class button():
    is_focused = False
    state = {True:2, False:1}
    content = ""
    pos_y = 0
    pos_x = 0
    window = None
    
    def __init__(self, window, pos_y, pos_y, content, name):

        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.window = window
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.content = content

    def toggle(self):
        self.is_focused = not self.is_focused
