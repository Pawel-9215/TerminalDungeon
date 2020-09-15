# This is place to add items for player to pick
from world_static import Pickable


class Dagger(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "W"
        self.name = "Dagger"
        self.strenght = 1


class Mace(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "W"
        self.name = "Mace"
        self.strenght = 1
