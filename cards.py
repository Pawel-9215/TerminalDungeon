from world_static import Pickable


class Card(Pickable):
    def __init__(self):
        super().__init__()
        self.destination = "deck"
        self.description = ["lin1", "lin2"]

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
                            "Deals 5 points of damage",
                            ]

    def on_deal(self):
        return {"attack": ["enemy", 5]}


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
        return {"heal": ["player", 4]}


class HealthDrain(Card):
    def __init__(self):
        super().__init__()
        self.glyph = "C"
        self.glyph_inverted = True
        self.glyph_color = "Red"
        self.name = "Health Drain"
        self.AP_cost = 4
        self.description = ["Cost : 4",
                            "Caster drains enemy's health",
                            "Drains 4 HP from to enemy",
                            "Restores 4 health points to caster"]

    def on_deal(self):
        return {"heal": ["player", 4],
                "drain": ["enemy", 4]}


class Poison(Card):
    def __init__(self):
        super().__init__()
        self.glyph = "C"
        self.glyph_inverted = True
        self.glyph_color = "Green"
        self.name = "Poison"
        self.AP_cost = 4
        self.description = ["Cost : 4",
                            "Enemy gets poisoned",
                            "Drains 1 HP each round for 4 rounds"]

    def on_deal(self):
        return {"poison": ["enemy", 4]}


class PoisonedBlade(Card):
    def __init__(self):
        super().__init__()
        self.glyph = "C"
        self.glyph_inverted = True
        self.glyph_color = "Green"
        self.name = "Poisoned Blade"
        self.AP_cost = 3
        self.description = ["Cost : 3",
                            "Caster hits enemy with poisoned blade",
                            "Enemy gets stabbed for 2 HP and poisoned",
                            "For 4 rounds"]
    def on_deal(self):
        return {"poison": ["enemy", 4],
                "attack": ["enemy", 2]}

class FullRecover(Card):
    def __init__(self):
        super().__init__()
        self.glyph = "C"
        self.glyph_inverted = True
        self.glyph_color = "Blue"
        self.name = "Full Recover"
        self.AP_cost = 4
        self.description = ["Cost : 4",
                            "Caster recovers his health",
                            "back to full",]
    def on_deal(self):
        return {"heal": ["player", 999]}

class PoisonousCloud(Card):
    def __init__(self):
        super().__init__()
        self.glyph = "C"
        self.glyph_inverted = True
        self.glyph_color = "Green"
        self.name = "Poisonous Cloud"
        self.AP_cost = 5
        self.description = ["Cost : 5",
                            "Poisonous cloud shrouds the battlefield",
                            "Caster get poisoned"
                            "for 7 rounds, and enemy looses 7 HP",
                            "at once"]
    def on_deal(self):
        return {"drain": ["enemy", 8],
                "poison": ["player", 8]}

class SacrificeKill(Card):
    def __init__(self):
        super().__init__()
        self.glyph = "C"
        self.glyph_inverted = True
        self.glyph_color = "Green"
        self.name = "Sacrifice Kill"
        self.AP_cost = 8
        self.description = ["Cost : 8",
                            "Enemy is hit with lethal amount of damage",
                            "Caster looses 10 HP points"]
    def on_deal(self):
        return {"attack": ["enemy", 99999],
                "drain": ["player", 10]}
