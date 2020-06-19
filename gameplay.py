import game_control
import map_loader




class GameInstance(game_control.Scene):
    def __init__(self, windows, name: str, engine: object):
        super().__init__(windows, name, engine)
        self.UI_window = self.windows[-1]  # window for UI data
        self.GP_window = self.windows[0]  # Gameplay window - map and player

    def load_map(self):
        pass
