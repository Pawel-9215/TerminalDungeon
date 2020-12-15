from world_static import Pickable
from player import Character


class Card(Pickable):
    def __init__(self):
        super().__init__()
        self.destination = "deck"
        self.AP_cost = 1
        self.description = "Card Description"

    def on_deal(self):
        return {"attack":3}

    def print_description(self):
        return self.description


# place to program collectable cards:

class Fireball(Card):
    def __init__(self):
        super().__init__()
        self.glyph = "C"
        self.glyph_inverted = True
        self.glyph_color = "Magenta"
        self.name = "Fireball"
        self.AP_cost = 2
        self.description = "Ball of fire appears and is thrusted\n"+"torwards the enemy"

    def on_deal(self):
        return {"attack":3}
