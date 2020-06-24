# This module should contain classes to create somewhat of main_menu
import curses
import game_control
import ui
import gameplay


class Credits(game_control.Scene):
    def __init__(self, windows, name: str, engine: object):
        super().__init__(windows, name, engine)
        self.print_content()
        self.updatable_objects.append(self)

    def print_content(self):
        start_pos_y = int(self.win_y / 6)
        start_pos_x = int(self.win_x / 6)
        credits = ["Code and Design: Pawel Hordyniak",
                   "Website: www.terminaldungeon.com",
                   "",
                   "Special Thanks to:",
                   "DmD",
                   "Bartek",
                   "ONE",
                   "Pawel",
                   ]

        info_bar = ui.Label(self.windows[0], "Credits:", start_pos_y, start_pos_x)
        for num, obj in enumerate(credits):
            self.renderable_objects.append(ui.Plain_text(self.windows[0], obj, start_pos_y + 1 + num, start_pos_x))

        self.renderable_objects.append(info_bar)

    def update(self, key):
        self.engine.change_scene(Mainmenu([self.engine.full_screen], "Main Menu", self.engine))
# go back to main-menu


class Mainmenu(game_control.Scene):

    def __init__(self, windows, name: str, engine: object):
        super().__init__(windows, name, engine)
        self.menu_items = ["New Game", "Credits", "Quit"]
        self.menu_buttons = []
        self.focused_item = 0
        self.test_gameplay = gameplay.GameInstance([self.engine.right_bar, self.engine.left_bar], "Gameplay", self.engine)
        self.credits_scene = Credits(self.windows, "Credits", self.engine)
        self.buttons_on_pressed = {
            "Quit": [quit, []],
            "New Game": [self.engine.change_scene, [self.test_gameplay]],
            "Credits": [self.engine.change_scene, [self.credits_scene]],
        }
        self.print_content()

    def print_content(self):
        start_pos_y = int(self.win_y / 2 - len(self.menu_items) / 2 - 1)
        start_pos_x = int(self.win_x / 4)

        for item in self.menu_items:
            self.menu_buttons.append(
                ui.button(self.windows[0], start_pos_y + self.menu_items.index(item), start_pos_x, item, item,
                          self.buttons_on_pressed[item][0], self.buttons_on_pressed[item][1]))
        self.renderable_objects.extend(self.menu_buttons)
        self.updatable_objects.append(self)
        self.menu_buttons[self.focused_item].is_focused = True

        instruction = ui.Plain_text(self.windows[0], " WSAD to move, spacebar to confirm ", self.win_y - 1, 2)
        self.renderable_objects.append(instruction)

        title_bar = ui.Label(self.windows[0], "  MAIN MENU           ", start_pos_y - 2, start_pos_x, bg="white")
        self.renderable_objects.append(title_bar)

    # self.manager.change_scene(self.credits2)

    def update(self, key):

        if key == "down":
            if self.focused_item + 1 > len(self.menu_buttons) - 1:
                self.focused_item = 0
            else:
                self.focused_item += 1

        if key == "up":
            if self.focused_item - 1 < 0:
                self.focused_item = len(self.menu_buttons) - 1
            else:
                self.focused_item -= 1

        if key == " ":
            self.menu_buttons[self.focused_item].on_pressed()

        for key in self.menu_buttons:
            key.is_focused = False
        self.menu_buttons[self.focused_item].is_focused = True
