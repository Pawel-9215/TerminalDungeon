#This module should contain classes to create somewhat of main_menu

import curses

class mainmenu():
	menu_items = ["New Game", "Options", "Load Game", "Quit"]
	win_y = 0
	win_x = 0
	win = None
	focused_item = 0
	
	def __init__(self, window):
		self.win = window
		curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
		self.win.clear()
		self.win.border()
		
		self.win_y, self.win_x = window.getmaxyx()
		
	def draw_item_list():
		pass