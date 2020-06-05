#This module should contain classes to create somewhat of main_menu
import curses
import game_control
import ui



class Credits(game_control.Scene):

	def print_content(self):
		start_pos_y = int(self.win_y/6)
		start_pos_x = int(self.win_x/6)
		credits = ["Code and Design: Pawel Hordyniak",
                           "Website: Pawel Hordyniak",
                           "",
                           "Special Thanks to:",
                           "DmD",
                           "Bartek",
                           "ONE",
                           "Pawel",
                           ]

		info_bar = ui.Label(self.windows[0], "Credits:", start_pos_y, start_pos_x)
		for num, obj in enumerate(credits):
                    self.renderable_objects.append(ui.Plain_text(self.windows[0], obj, start_pos_y+1+num, start_pos_x))
		
		self.renderable_objects.append(info_bar)

	def update(self, key):
		pass
		#go back to main-menu

class Mainmenu(game_control.Scene):
	menu_items = ["New Game", "Options", "Load Game", "Credits", "Quit"]
	menu_buttons = []
	win_y = 0
	win_x = 0
	focused_item = 0
	buttons_on_pressed = {}
	buttons_on_pressed = {
		"Quit":[quit, []],
		"New Game":[print, ['New Game']],
		"Options":[print, ['Options']],
		"Load Game":[print, ['Load Game']],
		"Credits":[print, ['dupa']],
		}
	"""
	def __init__(self):
		#super().__init__(windows, input_window, manager)
		self.win_y, self.win_x = self.windows[0].getmaxyx()
		self.manager = manager
		self.credits2 = Credits(self.windows, self.input_window, manager)
		
		self.draw_item_list()
	"""	
		
	def draw_item_list(self):
		start_pos_y = int(self.win_y/2-len(self.menu_items)/2-1)
		start_pos_x = int(self.win_x/4)

		for item in self.menu_items:
			self.menu_buttons.append(ui.button(self.windows[0], start_pos_y+self.menu_items.index(item), start_pos_x, item, item, self.buttons_on_pressed[item][0], self.buttons_on_pressed[item][1]))
		self.renderable_objects.extend(self.menu_buttons)
		self.updatable_objects.append(self)
		self.menu_buttons[self.focused_item].is_focused = True

		title_bar = ui.Label(self.windows[0], "  MAIN MENU           ", start_pos_y-2, start_pos_x, bg="white")
		self.renderable_objects.append(title_bar)
		#self.manager.change_scene(self.credits2)

	def update(self, key):

		if key == "down":
			if self.focused_item+1>len(self.menu_buttons)-1:
				self.focused_item = 0
			else:
				self.focused_item += 1

		if key == "up":
			if self.focused_item-1<0:
				self.focused_item = len(self.menu_buttons)-1
			else:
				self.focused_item -= 1

		if key == " ":
			self.menu_buttons[self.focused_item].on_pressed()

		

		for key in self.menu_buttons:
			key.is_focused = False
		self.menu_buttons[self.focused_item].is_focused = True




		


