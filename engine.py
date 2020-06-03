# So this is supposed to be engine class.
# We are going to store here a lot of shit :D and so on
import game_control
import ui

class Engine():
    def __init__(self, full_screen: object, left_bar: object, right_bar: object):
        self.full_screen = full_screen
        self.left_bar = left_bar
        self.right_bar = right_bar
        self.base_scene = game_control.Scene([full_screen], "Blank Page", self)
        self.current_scene = self.base_scene
        self.key_input = game_control.Keyboard(self)
        self.renderer = game_control.Renderque(self)
        self.updater = game_control.Updateque(self)




    def run_game(self):
        self.key_input.key_listen()
        self.updater.updatepass(self.key_input.last_pressed)
        self.renderer.renderpass()
        self.key_input.key_listen()