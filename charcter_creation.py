import ui
import game_control

class CharacterCreation(game_control.Scene):
    def __init__(self, windows, name: str, engine: object):
        super().__init__(windows, name, engine)
        self.updatable_objects.append(self)
        self.print_content()
        
    def print_content(self):

        header = ui.Plain_text(self.input_window, "Welcome to Character creation tool", 2, 4)
        self.renderable_objects.append(header)
        instruction = ui.Plain_text(self.input_window, "Please provide character name:", 3, 4)
        self.renderable_objects.append(instruction)

    def update(self, key):
        pass