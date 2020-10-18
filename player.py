"""
This is module for player class
"""
from __future__ import annotations


# ← ↑ → ↓

class Character:
    """
    Base class for characters - This should be inherited by both player and mobs alike
    """

    def __init__(self, y, x, glyph, world_map, game_instance):
        self.game_instance = game_instance
        self.y = y
        self.x = x
        self.glyph = glyph
        self.glyph_inverted = False
        self.glyph_color = "White"
        self.world_map = world_map
        self.look_at_y = self.y + 1
        self.look_at_x = self.x
        self.is_mob = True

        # character sheet:

        self.name = "Character"
        self.short_name = self.name[0:5]
        self.health = 10
        self.current_health = self.health
        self.melee_skill = 20
        self.action_points = 4
        self.strengh = 30
        self.endurance = 20
        self.hit_points = round(self.strengh/10)
        self.defence_points = round(self.endurance/10)

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

    def remove_self(self):
        self.vacate_position()
        self.world_map = None
        self.game_instance = None

    """def update(self, *args, **kwargs):
        
        pass"""
    
    def update_stats(self):
        self.hit_points = round(self.strengh/10)
        self.defence_points = round(self.endurance/10)

    """def move(self, direction):
        
        way_to_go = {"left": [0, -1, "←"], "right": [0, 1, "→"], "up": [-1, 0, "↑"], "down": [1, 0, "↓"]}
        if self.world_map.check_content(self.y + way_to_go[direction][0],
                                        self.x + way_to_go[direction][1]) == "free":
            self.vacate_position()
            self.y = self.y + way_to_go[direction][0]
            self.x = self.x + way_to_go[direction][1]
            self.update_position()

        # self.glyph = way_to_go[direction][2]
        self.look_at_y = self.y + way_to_go[direction][0]
        self.look_at_x = self.x + way_to_go[direction][1]"""

    def vacate_position(self):
        self.world_map.grid[self.y][self.x].occupation = "free"

    def update_position(self):
        self.world_map.grid[self.y][self.x].occupation = self

    def __str__(self):
        return self.name


class Player(Character):
    """
    Player class
    """

    def __init__(self, y, x, glyph, character_sheet, world_map, game_instance):
        super().__init__(y, x, glyph, world_map, game_instance)
        self.y = y
        self.x = x
        self.glyph = glyph
        self.glyph_color = "Red"
        self.glyph_inverted = True
        self.world_map = world_map
        self.look_at_y = self.y + 1
        self.look_at_x = self.x
        self.is_mob = False

        # character sheet:

        self.name = character_sheet["name"]
        self.short_name = self.name[0:6]
        self.health = character_sheet["health"]
        self.current_health = self.health
        self.melee_skill = character_sheet["melee"]
        self.action_points = character_sheet["action_points"]
        self.strengh = character_sheet["str"]
        self.endurance = character_sheet["end"]
        self.hit_points = round(self.strengh/10)
        self.defence_points = round(self.endurance/10)

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
        """
        This is logic of players character based on players input
        """

        if key in ["up", "down", "left", "right"]:
            self.move(key)
        elif key in ["1", "2", "3", "4"]:
            if key == "1" and self.inv_1 is not None:
                self.game_instance.ask_Dump_or_Equip(key)
            elif key == "2" and self.inv_2 is not None:
                self.game_instance.ask_Dump_or_Equip(key)
            elif key == "3" and self.inv_3 is not None:
                self.game_instance.ask_Dump_or_Equip(key)
            elif key == "4" and self.inv_4 is not None:
                self.game_instance.ask_Dump_or_Equip(key)
            else:
                pass
            
        elif key == " ":
            if self.world_map.grid[self.y][self.x].pickable != "free":
                self.pickup()
            else:
                self.use()
        else:
            pass

        self.game_instance.check_neighbours()
        self.hit_points = round(self.strengh/10)
        self.defence_points = round(self.endurance/10)


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

    def get_bodypart_state(self, bodypart: str):
        if bodypart == "weapon":
            return self.weapon
        elif bodypart == "arm_head":
            return self.arm_head
        elif bodypart  == "arm_torso":
            return self.arm_torso
        elif bodypart == "arm_hands":
            return self.arm_hands
        elif bodypart == "arm_legs":
            return self.arm_legs

    def set_bodypart_state(self, bodypart, item):
        if bodypart == "weapon":
            self.weapon = item
        elif bodypart == "arm_head":
            self.arm_head = item
        elif bodypart  == "arm_torso":
            self.arm_torso = item
        elif bodypart == "arm_hands":
            self.arm_hands = item
        elif bodypart == "arm_legs":
            self.arm_legs = item

    def get_inventory_state(self, item_slot):

        if item_slot == "1":
            return self.inv_1
        elif item_slot == "2":
            return self.inv_2
        elif item_slot == "3":
            return self.inv_3
        elif item_slot == "4":
            return self.inv_4
        else:
            pass

    def set_inventory_state(self, item_slot, item):

        if item_slot == "1":
            self.inv_1 = item
        elif item_slot == "2":
            self.inv_2 = item
        elif item_slot == "3":
            self.inv_3 = item
        elif item_slot == "4":
            self.inv_4 = item
        else:
            pass

    def pickup(self):

        object_to_pick = self.world_map.grid[self.y][self.x].pickable

        # check if default body part is available:

        if self.get_bodypart_state(object_to_pick.destination) is None:
            self.set_bodypart_state(object_to_pick.destination, object_to_pick)
        elif self.inv_1 is None:
            self.inv_1 = object_to_pick
        elif self.inv_2 is None:
            self.inv_2 = object_to_pick
        elif self.inv_3 is None:
            self.inv_3 = object_to_pick
        elif self.inv_4 is None:
            self.inv_4 = object_to_pick
        else:
            return "No place in inventory. Throw something out"
        self.world_map.grid[self.y][self.x].pickable = "free"
