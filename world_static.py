# Map classes


class Cell():
    def __init__(self, floor_glyph, occupation="free"):
        self.floor_glyph = floor_glyph
        self.occupation = occupation


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


class PlayerStart():
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def remove_self(self):
        # this should be replaced by reference to player instance
        # on game start
        pass
