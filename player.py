"""
This is module for player class
"""
from map_loader import WorldMap


# ← ↑ → ↓

class Character:
    """
    Base class for characters - This should be inherited by both player and mobs alike
    """

    def __init__(self, y, x, glyph, world_map: WorldMap):
        self.y = y
        self.x = x
        self.glyph = glyph
        self.world_map = world_map
        self.look_at_y = self.y + 1
        self.look_at_x = self.x

        # character sheet:

        self.name = "Character"
        self.health = 10
        self.melee_skill = 20
        self.action_points = 4
        self.strenght = 4
        self.endurance = 4

        # clothes:

        self.arm_head = None
        self.arm_torso = None
        self.arm_hands = None
        self.arm_legs = None

        # weapon

        self.weapon = None

        # inventory

        self.inv_1 = None
        self.inv_2 = None
        self.inv_3 = None
        self.inv_4 = None

    def update(self):
        pass

class Player:
    """
    Player class !warning - This needs refactor to inherit from character class
    """

    def __init__(self, y, x, glyph, character_sheet, world_map: WorldMap):
        self.y = y
        self.x = x
        self.glyph = glyph
        self.world_map = world_map
        self.look_at_y = self.y + 1
        self.look_at_x = self.x

        # character sheet:

        self.name = character_sheet["name"]
        self.health = character_sheet["health"]
        self.melee_skill = character_sheet["melee"]
        self.action_points = character_sheet["action_points"]
        self.strengh = character_sheet["str"]
        self.endurance = character_sheet["end"]

        # clothes:

        self.arm_head = character_sheet["arm_head"]
        self.arm_torso = character_sheet["arm_torso"]
        self.arm_hands = character_sheet["arm_hands"]
        self.arm_legs = character_sheet["arm_legs"]

        # weapon:

        self.weapon = character_sheet["weapon"]

        # inventory:

        self.inv_1 = character_sheet["inv_1"]
        self.inv_2 = character_sheet["inv_2"]
        self.inv_3 = character_sheet["inv_3"]
        self.inv_4 = character_sheet["inv_4"]

        # "save game"

        self.current_map = character_sheet["current_map"]

    def update(self, key):

        if key in ["up", "down", "left", "right"]:
            self.move(key)
        elif key == " ":
            self.use()
        else:
            pass
        pass

    def move(self, direction):
        """
        method to move player on grid
        """
        way_to_go = {"left": [0, -1, "←"], "right": [0, 1, "→"], "up": [-1, 0, "↑"], "down": [1, 0, "↓"]}
        if self.world_map.check_content(self.y + way_to_go[direction][0],
                                        self.x + way_to_go[direction][1]) == "free":
            self.vacate_position()
            self.y = self.y + way_to_go[direction][0]
            self.x = self.x + way_to_go[direction][1]
            self.update_position()

        self.glyph = way_to_go[direction][2]
        self.look_at_y = self.y + way_to_go[direction][0]
        self.look_at_x = self.x + way_to_go[direction][1]

    def vacate_position(self):

        self.world_map.grid[self.y][self.x].occupation = "free"

    def update_position(self):

        self.world_map.player_y = self.y
        self.world_map.player_x = self.x
        self.world_map.grid[self.y][self.x].occupation = self

    def use(self):

        if self.world_map.grid[self.look_at_y][self.look_at_x].occupation == "free":
            pass
        elif self.world_map.grid[self.look_at_y][self.look_at_x].occupation.destructable:
            self.world_map.grid[self.look_at_y][self.look_at_x].occupation = "free"
        else:
            pass
