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

    def print_content(self):

        welcome_lab = ui.Label(self.windows[0], 
                                "You reached new level!", 
                                self.start_pos[0],
                                self.start_pos[1])
        self.renderable_objects.append(welcome_lab)

        ui.button(self.windows[0],
                    self.start_pos[0]+2,
                    self.start_pos[1],
                    "+",
                    "add_health",
                    self.change_parameter,
                    [self.current_player.health, 1, 1, self.prev_health])
        ui.Plain_text(self.windows[0], "Health: "+str(self.current_player.health),
                    self.start_pos[0]+3, self.start_pos[1]+2)
        ui.button(self.windows[0],
                    self.start_pos[0]+4,
                    self.start_pos[1],
                    "-",
                    "substract_health",
                    self.change_parameter,
                    [self.current_player.health, -1, -1, self.prev_health])
        
    def change_parameter(self, parameter, cost, amount, min):
        if cost <= self.available_skillpoints and parameter+amount >= min:
            parameter = parameter + amount
            self.available_skillpoints -= cost

    def confirm(self):
        if self.available_skillpoints > 0:
            #skillpoints left!
            print("skillpoints left")
        else:
            pass
