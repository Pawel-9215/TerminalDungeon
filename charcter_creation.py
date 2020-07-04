import ui
import game_control
import curses

class CharacterCreation(game_control.Scene):
    def __init__(self, windows, name: str, engine: object):
        super().__init__(windows, name, engine)
        self.updatable_objects.append(self)
        self.focused_item = 0
        self.health = 10
        self.melee_skill = 0
        self.range_skill = 0
        self.strengh = 0
        self.endurance = 0
        self.buttons = []
        self.values = []
        self.character_name= "______"
        self.skill_points = 10
        self.print_content()
        
        
    def print_content(self):

        set_name = ui.button(self.windows[0], 3, 4, "Character Name", "character_name", self.set_name, [])
        self.buttons.append(set_name)
        self.renderable_objects.append(set_name)
        add_health = ui.button(self.windows[0], 4, 4, "+", "add_health", self.modify_param, [1, "health"])
        self.buttons.append(add_health)
        self.renderable_objects.append(add_health)
        health_par = ui.Plain_text(self.windows[0], "Health: ", 4, 6)
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
        
        
        
        self.print_values()

    def print_values(self):
        skill_points = ui.Plain_text(self.windows[0], "".join(["Available Skill Points: ", str(self.skill_points)]), 2, 4)
        self.renderable_objects.append(skill_points)
        self.values.append(skill_points)
        char_name = ui.Plain_text(self.windows[0], self.character_name, 3, 4+15)
        self.renderable_objects.append(char_name)
        self.values.append(char_name)
        health_val = ui.Plain_text(self.windows[0], str(self.health), 4, 14)
        self.renderable_objects.append(health_val)
        self.values.append(health_val)
        meelee_val = ui.Plain_text(self.windows[0], "".join(["Melee Skill: ", str(self.melee_skill)]), 6, 6)
        self.renderable_objects.append(meelee_val)
        self.values.append(meelee_val)
        range_val = ui.Plain_text(self.windows[0], "".join(["Range Skill: ", str(self.range_skill)]), 8, 6)
        self.renderable_objects.append(range_val)
        self.values.append(range_val)
        strengh_val = ui.Plain_text(self.windows[0], "".join(["Strengh: ", str(self.strengh)]), 10, 6)
        self.renderable_objects.append(strengh_val)
        self.values.append(strengh_val)
        endurance_val = ui.Plain_text(self.windows[0], "".join(["Endurance (End): ", str(self.endurance)]), 12, 6)
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
        self.character_name = self.windows[0].getstr(3, 4+15, 16)

    def modify_param(self, amount, param):
        if self.skill_points>0:
            if param == "health":
                self.health = self.health + amount
            elif param == "melee":
                self.melee_skill = self.melee_skill + amount
            elif param == "range":
                self.range_skill = self.range_skill + amount
            elif param == "strenght":
                self.strengh = self.strengh + amount
            elif param == "endurance":
                self.endurance = self.endurance + amount

            self.skill_points = self.skill_points - amount


