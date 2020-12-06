import game_control
import player
import ui

class LevelUpScene(game_control.Scene):
    def __init__(self, windows, name: str, engine: object, escape, player: player.Player):
        super().__init__(windows, name, engine)
        self.escape = escape
        self.current_player = player
        self.start_pos = [2, 4]

        self.available_skillpoints = 10

        #character old values
        self.prev_health = player.health
        self.prev_melee = player.melee_skill
        self.prev_ap = player.action_points
        self.prev_str = player.strengh

        self.parameters = Parameters(windows[0], self.current_player, self)
        self.print_content()

    def print_content(self):
        
        self.updatable_objects.append(self)
        self.renderable_objects.append(self.parameters)

        welcome_lab = ui.Label(self.windows[0], 
                                "You reached level "+str(self.current_player.level), 
                                self.start_pos[0],
                                self.start_pos[1])
        self.renderable_objects.append(welcome_lab)

        health_add = ui.button(self.windows[0],
                    self.start_pos[0]+2,
                    self.start_pos[1],
                    "+",
                    "add_health",
                    self.change_parameter,
                    ["health",1, 1, self.prev_health])
        health_sub = ui.button(self.windows[0],
                    self.start_pos[0]+4,
                    self.start_pos[1],
                    "-",
                    "substract_health",
                    self.change_parameter,
                    ["health",-1, -1, self.prev_health])

        self.renderable_objects.append(health_add)
        self.renderable_objects.append(health_sub)
        self.menu_buttons.append(health_add)
        self.menu_buttons.append(health_sub)

        melee_add = ui.button(self.windows[0],
                    self.start_pos[0]+5,
                    self.start_pos[1],
                    "+",
                    "add_melee",
                    self.change_parameter,
                    ["melee",1, 1, self.prev_melee])
        self.renderable_objects.append(melee_add)
        self.menu_buttons.append(melee_add)
        melee_sub = ui.button(self.windows[0],
                    self.start_pos[0]+7,
                    self.start_pos[1],
                    "-",
                    "sub_melee",
                    self.change_parameter,
                    ["melee",-1, -1, self.prev_melee])
        self.renderable_objects.append(melee_sub)
        self.menu_buttons.append(melee_sub)

        ap_add = ui.button(self.windows[0],
                    self.start_pos[0]+8,
                    self.start_pos[1],
                    "+",
                    "add_ap",
                    self.change_parameter,
                    ["ap",5, 1, self.prev_ap])
        self.renderable_objects.append(ap_add)
        self.menu_buttons.append(ap_add)
        ap_sub = ui.button(self.windows[0],
                    self.start_pos[0]+10,
                    self.start_pos[1],
                    "-",
                    "sub_ap",
                    self.change_parameter,
                    ["ap",-5, -1, self.prev_ap])
        self.renderable_objects.append(ap_sub)
        self.menu_buttons.append(ap_sub)

        str_add = ui.button(self.windows[0],
                    self.start_pos[0]+11,
                    self.start_pos[1],
                    "+",
                    "add_str",
                    self.change_parameter,
                    ["str",1, 1, self.prev_str])
        self.renderable_objects.append(str_add)
        self.menu_buttons.append(str_add)
        str_sub = ui.button(self.windows[0],
                    self.start_pos[0]+13,
                    self.start_pos[1],
                    "-",
                    "sub_str",
                    self.change_parameter,
                    ["str",-1, -1, self.prev_str])
        self.renderable_objects.append(str_sub)
        self.menu_buttons.append(str_sub)

    def change_parameter(self, par_name, cost, amount, min):

        if par_name == "health":
            if cost <= self.available_skillpoints and self.current_player.health+amount >= min:
                self.current_player.health += amount
                self.available_skillpoints -= cost

    def confirm(self):
        if self.available_skillpoints > 0:
            #skillpoints left!
            print("skillpoints left")
        else:
            pass

    def update(self, key):
        self.button_toggle(key)

class Parameters:
    def __init__(self, window, player: player.Player, levelup: LevelUpScene):
        self.window = window
        self.current_player = player
        self.levelupscene = levelup

    def draw(self):
        self.window.addstr(3, 6, "Available skillpoints: " + str(self.levelupscene.available_skillpoints))
        self.window.addstr(5, 6, "Health (Cost 1): " + str(self.current_player.health))
        self.window.addstr(8, 6, "Melee (Cost 1): " + str(self.current_player.melee_skill))
        self.window.addstr(11, 6, "Action Points (Cost 5): " + str(self.current_player.action_points))
        self.window.addstr(14, 6, "Strengh (Cost 1): "+ str(self.current_player.strengh))
        self.window.addstr(17, 6, "Endurance (Cost 1): " + str(self.current_player.endurance))

    def update(self):
        pass