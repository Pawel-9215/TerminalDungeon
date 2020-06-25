import game_control
import map_loader
import player


class GameInstance(game_control.Scene):
    """
    Game Instance - object for playthrough of a level
    """

    def __init__(self, windows, name: str, engine: object):
        super().__init__(windows, name, engine)
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
        self.current_player = player.Player(self.grid.player_y, self.grid.player_x, "↑")
        self.grid.grid[self.grid.player_y][self.grid.player_x].occupation = self.current_player

        grid_map = SituationMap(self.GP_window, self.grid, self)
        self.renderable_objects.append(grid_map)


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
                try:
                    self.window.addstr(y, x, str(self.grid.grid[y + diff_y][x + diff_x]))
                except:
                    self.window.addstr(y, x, "#")

                    # draw static map elements first, then dynamic objects like player

        # self.window.addstr(center_y, center_x, self.game_instance.current_player.glyph)
