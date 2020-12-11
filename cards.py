from world_static import Pickable
from player import Character


class Card(Pickable):
    def __init__(self):
        super(self).__init__()
        self.destination = "deck"
        self.attack = 0
        self.defence = 0
        self.is_instant = True
        self.ignore_defence = False


# place to program collectable cards:

class Fireball(Card):
    def __init__(self):
        super().__init__()
        self.glyph = "C"
        self.glyph_inverted = True
        self.glyph_color = "Magenta"
        self.name = "Fireball"
        self.attack = 3
        self.is_instant = True
        self.ignore_defence = False
