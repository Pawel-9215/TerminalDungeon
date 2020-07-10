# This module should contain classes to create somewhat of main_menu
import curses
import game_control
import ui
import gameplay
import charcter_creation
import pickle


class ChooseCharacter(game_control.Scene):
    def __init__(self, windows, name: str, engine: object, escape):
        super().__init__(windows, name, engine)
        self.escape = escape
        self.start_pos = (2, 4)
        self.updatable_objects.append(self)
        self.characters = self.load_characters()
        self.rotator = ui.Rotator(self.windows[0], list(self.characters.keys()), 4, 7)
        self.character_creator = charcter_creation.CharacterCreation(
            self.windows, "Character Creator", self.engine, self)
        self.buttons_names = [
            "↑", "↓", "Create new Character", "Start Game", "Return to Menu",
        ]
        self.buttons_on_pressed = {
            "↑": [self.rotator.rotate, [-1]],
            "↓": [self.rotator.rotate, [1]],
            "Create new Character": [self.engine.change_scene, [self.character_creator]],
            "Start Game": [print, ["Start Game"]],
            "Return to Menu": [self.engine.change_scene, [self.escape]],
        }
        self.print_content()

    def print_content(self):
        # huh
        extra = 0
        choose_char = ui.Plain_text(self.windows[0], "Choose character or create new one", self.start_pos[0],
                                    self.start_pos[1])
        self.renderable_objects.append(choose_char)
        for num, button in enumerate(self.buttons_names):

            if button == "↓" or button == "Create new Character":
                extra += 1
            self.menu_buttons.append(
                ui.button(self.windows[0],
                          self.start_pos[0] + 2 + num + extra,
                          self.start_pos[1],
                          button,
                          button,
                          self.buttons_on_pressed[button][0],
                          self.buttons_on_pressed[button][1],
                          ))
        for btn in self.menu_buttons:
            self.renderable_objects.append(btn)

        self.renderable_objects.append(self.rotator)



        self.menu_buttons[self.focused_item].is_focused = True

    def update(self, key):
        self.button_toggle(key)

    def load_characters(self):

        try:
            characters = pickle.load(open("resources/char", "rb"))
        except:
            characters = {"No characters": {"name": "No characters"}}

        return characters


class Credits(game_control.Scene):
    def __init__(self, windows, name: str, engine: object, escape):
        super().__init__(windows, name, engine)
        self.escape = escape
        self.print_content()
        self.updatable_objects.append(self)

    def print_content(self):
        start_pos_y = int(self.win_y / 6)
        start_pos_x = int(self.win_x / 6)
        game_credits = [
            "Code and Design: Pawel Hordyniak",
            "Website: www.terminaldungeon.com",
            "",
            "Special Thanks to:",
            "DmD",
            "Bartek",
            "ONE",
            "Pawel",
        ]

        info_bar = ui.Label(self.windows[0], "Credits:", start_pos_y, start_pos_x)
        for num, obj in enumerate(game_credits):
            self.renderable_objects.append(
                ui.Plain_text(self.windows[0], obj, start_pos_y + 1 + num, start_pos_x))

        self.renderable_objects.append(info_bar)

    def update(self, key):
        self.engine.change_scene(self.escape)


# go back to main-menu


class Mainmenu(game_control.Scene):
    def __init__(self, windows, name: str, engine: object):
        super().__init__(windows, name, engine)
        self.menu_items = ["Start Game", "Create Character", "Credits", "Quit"]
        self.menu_buttons = []
        self.focused_item = 0
        self.test_gameplay = gameplay.GameInstance(
            [self.engine.right_bar, self.engine.left_bar], "Gameplay", self.engine)
        self.character_creator = charcter_creation.CharacterCreation(
            self.windows, "Character Creator", self.engine, self)
        self.credits_scene = Credits(self.windows, "Credits", self.engine, self)
        self.char_choice = ChooseCharacter(self.windows, "Character Selection",
                                           self.engine, self)
        self.buttons_on_pressed = {
            "Quit": [quit, []],
            "Start Game": [self.engine.change_scene, [self.char_choice]],
            "Credits": [self.engine.change_scene, [self.credits_scene]],
            "Create Character": [self.engine.change_scene, [self.character_creator]],
        }
        self.print_content()

    def print_content(self):
        start_pos_y = int(self.win_y / 2 - len(self.menu_items) / 2 - 1)
        start_pos_x = int(self.win_x / 4)

        for item in self.menu_items:
            self.menu_buttons.append(
                ui.button(self.windows[0], start_pos_y + self.menu_items.index(item),
                          start_pos_x, item, item, self.buttons_on_pressed[item][
                              0], self.buttons_on_pressed[item][1]))
        self.renderable_objects.extend(self.menu_buttons)
        self.updatable_objects.append(self)
        self.menu_buttons[self.focused_item].is_focused = True

        instruction = ui.Plain_text(
            self.windows[0], " WSAD to move, spacebar to confirm ", self.win_y - 1, 2)
        self.renderable_objects.append(instruction)

        title_bar = ui.Label(
            self.windows[0],
            "  MAIN MENU           ",
            start_pos_y - 2,
            start_pos_x,
            bg="white")
        self.renderable_objects.append(title_bar)

    # self.manager.change_scene(self.credits2)

    def update(self, key):
        self.button_toggle(key)
