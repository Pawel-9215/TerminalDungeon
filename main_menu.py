#This module should contain classes to create somewhat of main_menu
import curses
import game_control
import ui

class Mainmenu(game_control.Scene):
	menu_items = ["New Game", "Options", "Load Game", "Credits", "Quit"]
	menu_buttons = []
	win_y = 0
	win_x = 0
	focused_item = 0
	
	def __init__(self,  windows, input_window):
		super().__init__(self,  windows, input_window)
		self.win_y, self.win_x = self.windows[0].getmaxyx()
		self.draw_item_list()
		
	def draw_item_list(self):
		start_pos_y = int(win_y/2-len(self.menu_items)/2-1)
		start_pos_x = int(win_x/6)

		for item in self.menu_items:
			self.menu_buttons.append(ui.button(self.windows[0], start_pos_y+self.menu_items.index(item), start_pos_x, item, item))
		self.renderable_objects = self.menu_buttons


