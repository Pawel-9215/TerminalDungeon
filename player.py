"""
This is module for player class
"""
from map_loader import WorldMap

# ← ↑ → ↓


class Player():
    """
    PLayer class
    """

    def __init__(self, y, x, glyph, world_map:WorldMap):
        self.y = y
        self.x = x
        self.glyph = glyph
        self.world_map = world_map

    def update(self):
        pass

    def move(self, direction):
        """
        method to move player on grid
        """
        self.vacate_position()

        if direction == "left":
            self.x -= 1
            self.glyph = "←"
        elif direction == "right":
            self.x += 1
            self.glyph = "→"
        elif direction == "up":
            self.y -= 1
            self.glyph = "↑"
        elif direction == "down":
            self.y += 1
            self.glyph = "↓"

        self.update_position()

    def vacate_position(self):

        self.world_map.grid[self.y][self.x].occupation = "free"

    def update_position(self):

        self.world_map.player_y = self.y
        self.world_map.player_x = self.x
        self.world_map.grid[self.y][self.x].occupation = self
