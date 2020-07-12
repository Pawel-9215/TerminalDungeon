# Map classes


class Cell():
    def __init__(self, floor_glyph, occupation="free"):
        self.floor_glyph = floor_glyph
        self.occupation = occupation
        self.pickable = None

    def __repr__(self):
        if self.occupation != "free":
            return self.occupation.glyph
        else:
            return self.floor_glyph

    def check_if_empty(self):
        if self.occupation == "free":
            return True
        else:
            return self.occupation


class SolidBody():
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


class PlayerStart():
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
