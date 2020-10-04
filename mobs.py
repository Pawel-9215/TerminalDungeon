"""This is were we ad basic mobs"""
from __future__ import annotations
from player import Character
import random

rat_names = ["Feskit", "Tredkit", "Paskrokin", "Rikeskit", "Morskit",
             "Ratchit", "Quoto", "Quotisk", "Paskratt", "Quorkat",
             "Trakat", "Dragkirt"]


# Basic level 1 mobs:

class Rat(Character):
    def __init__(self, y, x, glyph, world_map, game_instance):
        super().__init__(y, x, glyph, world_map, game_instance)
        self.glyph = "R"
        global rat_names
        self.short_name = random.choice(rat_names)
        self.name = self.short_name+" the Rat"
        self.endurance = 8
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
