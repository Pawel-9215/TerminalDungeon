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
        self.description = ["Cost: 2",
                            "Ball of fire appears and is thrown", 
                            "towards the enemy",
                            "Deals 5 points of damage"
                            ]

    def on_deal(self):
        return {"attack": 5}

class HealingRay(Card):
    def __init__(self):
        super().__init__()
        self.glyph = "C"
        self.glyph_inverted = True
        self.glyph_color = "Blue"
        self.name = "Healing Ray"
        self.AP_cost = 3
        self.description = ["Cost : 3", "Ray heals caster", "Restores 4 health points"]

    def on_deal(self):
        return {"heal": 4}
