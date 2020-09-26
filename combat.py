import game_control
import player


class CombatScreen(game_control.Scene):
    def __init__(self, windows,
                 name: str, engine: object,
                 escape,
                 current_player: player.Player,
                 current_enemy: player.Character):
        super().__init__(windows, name, engine)
        self.current_player = current_player
        self.current_enemy = current_enemy
        self.escape = escape
        self.player_sheet = CombatPlayerStats(windows[0], self.current_player, self)
        self.draw_content()

    def draw_content(self):

        self.updatable_objects.append(self)
        self.renderable_objects.append(self.player_sheet)

    def print_player_stats(self):
        self.player_sheet.draw()

    def update(self, key):
        # debug:
        if key == "l":
            self.engine.change_scene(self.escape)
        else:
            pass


class CombatPlayerStats:
    def __init__(self, window, current_player, combat_screen: CombatScreen):
        self.window = window
        self.current_player = current_player
        self.combat_screen = combat_screen
        self.window_y, self.window_x = window.getmaxyx()
        self.current_action_points = self.current_player.action_points

    def draw(self):

        min_y = 1
        max_y = self.window_y - 1
        min_x = 1
        max_x = self.window_x - 1
        center_y = int(self.window_y / 2)
        center_x = int(self.window_x / 2)

        # Name
        self.window.addstr(min_y+1, min_x+1, self.current_player.name)
        
        # Parameters
        self.window.addstr(min_y+3, min_x+1, ("HEALTH: "+str(self.current_player.current_health)+"/"+str(self.current_player.health)))
        self.window.addstr(min_y+4, min_x+1, ("MELEE: "+str(self.current_player.melee_skill)))
        self.window.addstr(min_y+5, min_x+1, ("AP: "+str(self.current_action_points)+"/"+str(self.current_player.action_points)))
        self.window.addstr(min_y+6, min_x+1, ("STRENGHT: "+str(self.current_player.strenght)))
        self.window.addstr(min_y+7, min_x+1, ("ENDURANCE: "+str(self.current_player.melee_skill)))

    def update(self, key):
        pass