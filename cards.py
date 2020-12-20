from world_static import Pickable


class Card(Pickable):
    def __init__(self):
        super().__init__()
        self.destination = "deck"
        self.description = "Card Description"

    def __repr__(self):
        return self.name

    def on_deal(self):
        return {"attack": 3}

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
        self.description = "Ball of fire appears and is thrown\n" + "towards the enemy"

    def on_deal(self):
        return {"attack": 5}
