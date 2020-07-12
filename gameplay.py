import game_control
import map_loader
import player


class GameInstance(game_control.Scene):
    """
    Game Instance - object for playthrough of a level
    """

    def __init__(self, windows, name: str, engine: object, character_sheet):
        super().__init__(windows, name, engine)
        self.character_sheet = character_sheet
        self.UI_window = self.windows[-1]  # window for UI data
        self.GP_window = self.windows[0]  # Gameplay window - map and player
        self.grid = None
        self.current_player = None
        self.load_map("Test_map_1")

    def load_map(self, map_name: "str"):
        """
        This loads map and sets reference in game instance
        """
        self.grid = map_loader.WorldMap(map_name)
        self.current_player = player.Player(self.grid.player_y,
                                            self.grid.player_x,
                                            "↑",
                                            self.character_sheet,
                                            self.grid)
        self.grid.grid[self.grid.player_y][self.grid.player_x].occupation = self.current_player

        grid_map = SituationMap(self.GP_window, self.grid, self)
        self.renderable_objects.append(grid_map)
        character_info = CharacterSheet(self.UI_window, self)
        self.renderable_objects.append(character_info)
        self.updatable_objects.append(self.current_player)


class CharacterSheet():
    """
    UI info in the left window
    """

    def __init__(self, window, game_instance: GameInstance):
        self.window = window
        self.window_y, self.window_x = window.getmaxyx()
        self.game_instance = game_instance

    def draw(self):
        min_y = 1
        max_y = self.window_y - 1
        min_x = 1
        max_x = self.window_x - 1
        center_y = int(self.window_y / 2)
        center_x = int(self.window_x / 2)

        self.window.addstr(min_y, center_x-3, "Hp:" + str(self.game_instance.current_player.health))
        self.window.addstr(2, min_x, "Mel:" + str(self.game_instance.current_player.melee_skill))
        self.window.addstr(2, max_x-len("Ran:" + str(self.game_instance.current_player.range_skill)),
                           "Ran:" + str(self.game_instance.current_player.range_skill))
        self.window.addstr(3, min_x, "Str:"+str(self.game_instance.current_player.strengh))
        self.window.addstr(3, max_x-len("End:" + str(self.game_instance.current_player.endurance)),
                           "End:" + str(self.game_instance.current_player.endurance))

        self.window.addstr(4,
                           int(center_x-len("Head:["+str(self.game_instance.current_player.arm_head)+"]")/2),
                           "Head:["+str(self.game_instance.current_player.arm_head)+"]")
        self.window.addstr(5,
                           int(center_x - len("Torso:[" + str(self.game_instance.current_player.arm_torso) + "]") / 2),
                           "Torso:[" + str(self.game_instance.current_player.arm_torso) + "]")
        self.window.addstr(6,
                           int(center_x - len("Hands:[" + str(self.game_instance.current_player.arm_hands) + "]") / 2),
                           "Hands:[" + str(self.game_instance.current_player.arm_hands) + "]")
        self.window.addstr(7,
                           int(center_x - len("Legs:[" + str(self.game_instance.current_player.arm_legs) + "]") / 2),
                           "Legs:[" + str(self.game_instance.current_player.arm_legs) + "]")

        self.window.addstr(9,
                           int(center_x - len("Weapon:[" + str(self.game_instance.current_player.weapon) + "]") / 2),
                           "Weapon:[" + str(self.game_instance.current_player.weapon) + "]")
        self.window.addstr(10, min_x, "Inventory:")
        self.window.addstr(11, min_x, "1:["+str(self.game_instance.current_player.inv_1)+"]")
        self.window.addstr(11, max_x-(len("2:[" + str(self.game_instance.current_player.inv_2) + "]")), "2:[" + str(self.game_instance.current_player.inv_2) + "]")
        self.window.addstr(12, min_x, "3:[" + str(self.game_instance.current_player.inv_3) + "]")
        self.window.addstr(12, max_x - (len("3:[" + str(self.game_instance.current_player.inv_3) + "]")),
                           "3:[" + str(self.game_instance.current_player.inv_3) + "]")


class SituationMap:
    """
    This is object responsible for drawing main gameplay window
    """

    def __init__(self, window, grid, game_instance: GameInstance):
        self.window = window
        self.grid = grid
        self.window_y, self.window_x = window.getmaxyx()
        self.game_instance = game_instance

    def draw(self):
        """
        this method is required in all object that are
        to be addet to renderable list of the scene
        """
        min_y = 1
        max_y = self.window_y - 1
        min_x = 1
        max_x = self.window_x - 1
        center_y = int(self.window_y / 2)
        center_x = int(self.window_x / 2)

        # get beginning
        diff_y = self.grid.player_y - center_y
        diff_x = self.grid.player_x - center_x

        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                if 0 < y + diff_y < len(self.grid.grid) and 0 < x + diff_x < len(self.grid.grid[y]):
                    self.window.addstr(y, x, str(self.grid.grid[y + diff_y][x + diff_x]))
                else:
                    self.window.addstr(y, x, "#")

                    # draw static map elements first, then dynamic objects like player

        # self.window.addstr(center_y, center_x, self.game_instance.current_player.glyph)
