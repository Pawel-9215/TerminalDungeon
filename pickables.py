# This is place to add items for player to pick
import random
from world_static import Pickable


class Dagger(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "W"
        self.glyph_inverted = True
        self.glyph_color = "Yellow"
        self.name = "Dagger"
        self.strenght = (1, 2)


class Mace(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "W"
        self.glyph_inverted = True
        self.glyph_color = "Magenta"
        self.name = "Mace"
        self.strenght = (0, 2)

class Helmet(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "A"
        self.glyph_inverted = False
        self.glyph_color = "Yellow"
        self.name = "Helmet"
        self.destination = "arm_head"
        self.defence_points = random.randint(1, 2)
