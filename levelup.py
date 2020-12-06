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

        self.parameters = Parameters(windows[0], self.current_player, self)
        self.print_content()

    def print_content(self):
        
        self.updatable_objects.append(self)
        self.renderable_objects.append(self.parameters)

        welcome_lab = ui.Label(self.windows[0], 
                                "You reached new level!", 
                                self.start_pos[0],
                                self.start_pos[1])
        self.renderable_objects.append(welcome_lab)

        health_add = ui.button(self.windows[0],
                    self.start_pos[0]+2,
                    self.start_pos[1],
                    "+",
                    "add_health",
                    self.change_parameter,
                    ["health", self.current_player.health, 1, 1, self.prev_health])
        health_sub = ui.button(self.windows[0],
                    self.start_pos[0]+4,
                    self.start_pos[1],
                    "-",
                    "substract_health",
                    self.change_parameter,
                    ["health", self.current_player.health, -1, -1, self.prev_health])

        self.renderable_objects.append(health_add)
        self.renderable_objects.append(health_sub)
        self.menu_buttons.append(health_add)
        self.menu_buttons.append(health_sub)


    def change_parameter(self, par_name, parameter, cost, amount, min):
        if cost <= self.available_skillpoints and parameter+amount >= min:
            parameter = parameter + amount
            self.available_skillpoints -= cost

        if par_name == "health":
            self.current_player.health = parameter

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
        self.window.addstr(5, 6, "Health: " + str(self.current_player.health))
        self.window.addstr(8, 6, "Melee: " + str(self.current_player.melee_skill))

    def update(self):
        pass