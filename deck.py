# This should be the place for deck related things from the very beginning
import ui
import player
import game_control


class DeckView(game_control.Scene):
    def __init__(self, windows, name, engine, player: player.Player, escape: game_control.Scene):
        super().__init__(windows, name, engine)
        self.current_player = player
        self.escape = escape
        self.max_y, self.max_x = self.windows[0].getmaxyx()
        self.rotator = ui.Rotator(self.windows[0], self.current_player.deck, 3, int(self.max_x/2-4))
        self.buttons = {
            "↑":[self.rotator.rotate, [-1]],
            "↓":[self.rotator.rotate, [1]],
            "Destroy Card":[self.destroy_card, []],
            "Back": [self.engine.change_scene, [self.escape]],
        }
        self.print_content()

    def print_content(self):
        self.renderable_objects.append(self.rotator)
    
    def destroy_card(self):
        pass

    def update_rotator(self):
        pass
