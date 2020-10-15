# Map classes
from __future__ import annotations
import random


class Cell:
    def __init__(self, floor_glyph, occupation="free"):
        self.floor_glyph = floor_glyph
        self.occupation = occupation
        self.pickable = "free"
        self.distance_to_player = 255

    def __repr__(self):
        if self.occupation != "free":
            return self.occupation.glyph
        elif self.pickable != "free":
            return self.pickable.glyph
        else:
            return self.floor_glyph

    def check_if_empty(self):
        if self.occupation == "free":
            return True
        else:
            return self.occupation


class SolidBody:
    def __init__(self):
        self.destructable = False
        self.glyph = "@"
        self.health = 10

    def on_hit(self, hit_points):
        if self.destructable is True and self.health > 0:
            self.health = self.health - hit_points


class Rock(SolidBody):
    def __init__(self):
        super().__init__()
        self.descructable = True


class StoneWall(SolidBody):
    def __init__(self):
        super().__init__()
        self.glyph = "█"
        self.destructable = True


class PlayerStart:
    """
    This object should be replaced by player class when the game starts.
    """

    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.glyph = "P"

    def remove_self(self):
        # this should be replaced by reference to player instance
        # on game start
        del self


class Pickable:
    def __init__(self):
        self.glyph = "P"
        self.glyph_inverted = False
        self.glyph_color = "White"
        self.destination = "weapon"
        self.consumable = False
        self.name = "Pickable"

        # player mod:

        self.health = 0
        self.strenght = (0, 0)
        self.defence_points = 0

    def __repr__(self):
        return self.name
    
    def weapon_attack(self):
        return random.randint(self.strenght[0], self.strenght[1])
