import ui
import game_control
import curses
import random
import pickle

class CharacterCreation(game_control.Scene):
    def __init__(self, windows, name: str, engine: object):
        super().__init__(windows, name, engine)
        self.updatable_objects.append(self)
        self.focused_item = 0
        self.health = 5 + random.randint(2, 20)
        self.melee_skill = 20 + random.randint(2, 20)
        self.range_skill = 20 + random.randint(2, 20)
        self.strengh = random.randint(10, 60)
        self.endurance = random.randint(10, 30)
        self.buttons = []
        self.values = []
        self.character_name= "______"
        self.skill_points = 10
        self.print_content()
        self.initial_values = {
            "health":self.health,
            "melee":self.melee_skill,
            "range":self.range_skill,
            "strengh":self.strengh,
            "endurance":self.endurance,
        }
        
        
    def print_content(self):

        set_name = ui.button(self.windows[0], 3, 4, "Character Name", "character_name", self.set_name, [])
        self.buttons.append(set_name)
        self.renderable_objects.append(set_name)
        add_health = ui.button(self.windows[0], 4, 4, "+", "add_health", self.modify_param, [1, "health"])
        self.buttons.append(add_health)
        self.renderable_objects.append(add_health)
        health_par = ui.Plain_text(self.windows[0], "Health (Hp): ", 4, 6)
        self.renderable_objects.append(health_par)
        substract_health = ui.button(self.windows[0], 5, 4, "-", "substract_health", self.modify_param, [-1, "health"])
        self.buttons.append(substract_health)
        self.renderable_objects.append(substract_health)
        add_melee = ui.button(self.windows[0], 6, 4, "+", "add_melee", self.modify_param, [1, "melee"])
        self.buttons.append(add_melee)
        self.renderable_objects.append(add_melee)
        substract_melee = ui.button(self.windows[0], 7, 4, "-", "substract_melee", self.modify_param, [-1, "melee"])
        self.buttons.append(substract_melee)
        self.renderable_objects.append(substract_melee)
        add_range = ui.button(self.windows[0], 8, 4, "+", "add_range", self.modify_param, [1, "range"])
        self.buttons.append(add_range)
        self.renderable_objects.append(add_range)
        substract_range = ui.button(self.windows[0], 9, 4, "-", "substract_range", self.modify_param, [-1, "range"])
        self.buttons.append(substract_range)
        self.renderable_objects.append(substract_range)
        add_strengh = ui.button(self.windows[0], 10, 4, "+", "add_strenght", self.modify_param, [1, "strengh"])
        self.buttons.append(add_strengh)
        self.renderable_objects.append(add_strengh)
        substract_strengh = ui.button(self.windows[0], 11, 4, "-", "substract_strenght", self.modify_param, [-1, "strengh"])
        self.buttons.append(substract_strengh)
        self.renderable_objects.append(substract_strengh)
        add_endurance = ui.button(self.windows[0], 12, 4, "+", "add_endurance", self.modify_param, [1, "endurance"])
        self.buttons.append(add_endurance)
        self.renderable_objects.append(add_endurance)
        substract_endurance = ui.button(self.windows[0], 13, 4, "-", "substract_endurance", self.modify_param, [-1, "endurance"])
        self.buttons.append(substract_endurance)
        self.renderable_objects.append(substract_endurance)

        accept_btn = ui.button(self.windows[0], 15, 4, "Accept", "accept", self.save_character, [])
        self.renderable_objects.append(accept_btn)
        self.buttons.append(accept_btn)
        
        
        self.buttons[self.focused_item].is_focused = True

        self.print_values()

    def print_values(self):
        skill_points = ui.Plain_text(self.windows[0], "".join(["Available Skill Points: ", str(self.skill_points)]), 2, 4)
        self.renderable_objects.append(skill_points)
        self.values.append(skill_points)
        char_name = ui.Plain_text(self.windows[0], self.character_name, 3, 4+15)
        self.renderable_objects.append(char_name)
        self.values.append(char_name)
        health_val = ui.Plain_text(self.windows[0], str(self.health), 4, 20)
        self.renderable_objects.append(health_val)
        self.values.append(health_val)
        meelee_val = ui.Plain_text(self.windows[0], "".join(["Melee Skill (Mel): ", str(self.melee_skill)]), 6, 6)
        self.renderable_objects.append(meelee_val)
        self.values.append(meelee_val)
        range_val = ui.Plain_text(self.windows[0], "".join(["Range Skill (Rng): ", str(self.range_skill)]), 8, 6)
        self.renderable_objects.append(range_val)
        self.values.append(range_val)
        strengh_val = ui.Plain_text(self.windows[0], "".join(["Strengh (Str): ", str(self.strengh), " Actual/10: ", str(round(self.strengh/10))]), 10, 6)
        self.renderable_objects.append(strengh_val)
        self.values.append(strengh_val)
        endurance_val = ui.Plain_text(self.windows[0], "".join(["Endurance (End): ", str(self.endurance), " Actual/10: ", str(round(self.endurance/10))]), 12, 6)
        self.renderable_objects.append(endurance_val)
        self.values.append(endurance_val)


    def update(self, key):

        if key == "down":
            if self.focused_item + 1 > len(self.buttons) - 1:
                self.focused_item = 0
            else:
                self.focused_item += 1

        if key == "up":
            if self.focused_item - 1 < 0:
                self.focused_item = len(self.buttons) - 1
            else:
                self.focused_item -= 1

        if key == " ":
            self.buttons[self.focused_item].on_pressed()

        for key in self.buttons:
            key.is_focused = False
        self.print_values()
        self.buttons[self.focused_item].is_focused = True
        for value in self.values:
                    self.renderable_objects.remove(value)
        self.values.clear()
        self.print_values()


    def set_name(self):
        self.character_name = ""
        self.update("none")
        self.engine.renderer.renderpass()
        curses.echo()
        self.character_name = self.windows[0].getstr(3, 4+15, 16).decode('utf-8')

    def modify_param(self, amount, param):
        if (self.skill_points>0 and amount == 1) or (self.skill_points<10 and amount == -1):
            if param == "health" and ((self.health > self.initial_values[param] and amount == -1) or amount == 1):
                self.health = self.health + amount
                self.skill_points = self.skill_points - amount
            elif param == "melee" and ((self.melee_skill > self.initial_values[param] and amount == -1) or amount == 1):
                self.melee_skill = self.melee_skill + amount
                self.skill_points = self.skill_points - amount
            elif param == "range" and ((self.range_skill > self.initial_values[param] and amount == -1) or amount == 1):
                self.range_skill = self.range_skill + amount
                self.skill_points = self.skill_points - amount
            elif param == "strengh" and ((self.strengh > self.initial_values[param] and amount == -1) or amount == 1):
                self.strengh = self.strengh + amount
                self.skill_points = self.skill_points - amount
            elif param == "endurance" and ((self.endurance > self.initial_values[param] and amount == -1) or amount == 1):
                self.endurance = self.endurance + amount
                self.skill_points = self.skill_points - amount

    def save_character(self):
        try:
            characters = pickle.load(open("resources/char", "rb"))
        except:
            pickle.dump({}, open("resources/char", "wb"))
            characters = pickle.load(open("resources/char", "rb"))

        try:
            check = characters[self.character_name]
            warning = ui.Label(self.windows[0], "Character with that name already exists!/n Pick different name!", int(self.win_y/2), int(self.win_x/2-20))
            self.renderable_objects.append(warning)
            self.values.append(warning)
            self.engine.renderer.renderpass()
        except:
            character = {
                "name":self.character_name,
                "health":self.health,
                "melee":self.melee_skill,
                "range":self.range_skill,
                "str":self.strengh,
                "end":self.endurance,
                "arm_head":None,
                "arm_torso":None,
                "arm_hands":None,
                "arm_legs":None,
                "weapon":None,
                "inv_1":None,
                "inv_2":None,
                "inv_3":None,
                "inv_4":None,
                "current_map":1
            }
            characters[self.character_name] = character
            pickle.dump(characters, open("resources/char", "wb"), -1)

            


