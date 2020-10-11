"""This is were we ad basic mobs"""
from __future__ import annotations
from player import Character
import random

rat_names1 = ["Fes", "Tred", "Paskro", "Rikes", "Mors",
              "Rat", "Quo", "Quot", "Pask", "Quar",
              "Tra", "Drag", "Derg", "Pesk", "Fas",
              "Trud", "Rekis", "Murs", "Ret"]
rat_names2 = ["kit", "kin", "chit", "oto", "isk", "ratt", "krat", "akat", "kirt", "rit", "tirt", "irt"]


# Basic level 1 mobs:

class Rat(Character):
    def __init__(self, y, x, glyph, world_map, game_instance):
        super().__init__(y, x, glyph, world_map, game_instance)
        self.glyph = "R"
        self.glyph_color = "Red"
        global rat_names1, rat_names2
        self.short_name = random.choice(rat_names1)+random.choice(rat_names2)
        self.name = self.short_name + " the Rat"
        self.endurance = random.randint(7, 10)
        self.health = random.randint(7, 12)
        self.melee_skill = random.randint(15, 25)
        self.update_stats()

    def update(self, *args, **kwargs):
        directions = ["up", "down", "left", "right"]

        chosen_dir = random.choice(directions)
        self.move(chosen_dir)

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

        # self.glyph = way_to_go[direction][2] - can't change mob glyph to players
        self.look_at_y = self.y + way_to_go[direction][0]
        self.look_at_x = self.x + way_to_go[direction][1]


class RatWarrior(Character):
    def __init__(self, y, x, glyph, world_map, game_instance):
        super().__init__(y, x, glyph, world_map, game_instance)
        self.glyph = "R"
        self.glyph_color = "Red"
        self.glyph_inverted = True
        self.action_points = 5
        global rat_names1, rat_names2
        self.short_name = random.choice(rat_names1)+random.choice(rat_names2)
        self.name = "RatWarrior "+ self.short_name
        self.endurance = random.randint(12, 16)
        self.health = random.randint(12, 16)
        self.melee_skill = random.randint(26, 32)
        self.update_stats()

    def update(self, *args, **kwargs):
        directions = ["up", "down", "left", "right"]

        chosen_dir = random.choice(directions)
        self.move(chosen_dir)

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

        # self.glyph = way_to_go[direction][2] - can't change mob glyph to players
        self.look_at_y = self.y + way_to_go[direction][0]
        self.look_at_x = self.x + way_to_go[direction][1]
