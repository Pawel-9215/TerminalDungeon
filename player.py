"""
This is module for player class
"""
from map_loader import WorldMap

# ← ↑ → ↓


class Player():
    """
    Player class
    """

    def __init__(self, y, x, glyph, character_sheet, world_map:WorldMap):
        self.y = y
        self.x = x
        self.glyph = glyph
        self.world_map = world_map

        # character sheet:

        self.name = character_sheet["name"]
        self.health = character_sheet["health"]
        self.melee_skill = character_sheet["melee"]
        self.range_skill = character_sheet["range"]
        self.strengh = character_sheet["str"]
        self.endurance = character_sheet["end"]

        # clothes:

        self.arm_head = character_sheet["arm_head"]
        self.arm_torso = character_sheet["arm_torso"]
        self.arm_hands = character_sheet["arm_hands"]
        self.arm_legs = character_sheet["arm_legs"]


    def update(self, key):

        if key in ["up", "down", "left", "right"]:
            self.move(key)
        else:
            pass
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
