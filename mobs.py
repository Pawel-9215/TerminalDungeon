"""This is were we ad basic mobs"""
from __future__ import annotations
from player import Character
import random
import cards

rat_names1 = ["Fes", "Tred", "Paskro", "Rikes", "Mors",
              "Rat", "Quo", "Quot", "Pask", "Quar",
              "Tra", "Drag", "Derg", "Pesk", "Fas",
              "Trud", "Rekis", "Murs", "Ret"]
rat_names2 = ["kit", "kin", "chit", "oto", "isk", "ratt", "krat", "akat", "kirt", "rit", "tirt", "irt"]

goblin_names = ["Ois", "Blong", "Kord", "Vrilx", "Bong", "Freklucs", "Iknoc",
                "Jiorgug", "Pobkalk", "Klaatmyrd"]


# Basic level 1 mobs:

class Rat(Character):
    def __init__(self, y, x, world_map, game_instance):
        super().__init__(y, x, world_map, game_instance)
        self.glyph = "R"
        self.glyph_color = "Red"
        global rat_names1, rat_names2
        self.short_name = random.choice(rat_names1) + random.choice(rat_names2)
        self.name = self.short_name + " the Rat"
        self.endurance = random.randint(3, 6)
        self.health = random.randint(4, 10)
        self.melee_skill = random.randint(15, 25)
        self.distance_to_player = 255
        self.update_stats()
        self.EXP_value = 10
        self.on_create()

    def update(self, *args, **kwargs):
        directions = ["up", "down", "left", "right", "stop"]

        # check distance to player

        self.distance_to_player = self.world_map.check_distance_to_player(self.y, self.x)
        print(self.distance_to_player)

        if self.distance_to_player < 12:
            chosen_dir = self.escape_player(directions)
        else:
            chosen_dir = random.choice(directions)
            # chosen_dir = "stop"

        # chosen_dir = random.choice(directions)
        # chosen_dir = "stop"
        self.move(chosen_dir)


class RatWarrior(Character):
    def __init__(self, y, x, world_map, game_instance):
        super().__init__(y, x, world_map, game_instance)
        self.glyph = "R"
        self.glyph_color = "Red"
        self.glyph_inverted = True
        self.action_points = 5
        global rat_names1, rat_names2
        self.short_name = random.choice(rat_names1) + random.choice(rat_names2)
        self.name = "RatWarrior " + self.short_name
        self.endurance = random.randint(12, 16)
        self.health = random.randint(12, 16)
        self.melee_skill = random.randint(26, 32)
        self.distance_to_player = 255
        self.update_stats()
        self.EXP_value = 20
        self.on_create()
        self.deck = [cards.Fireball()]

    def update(self, *args, **kwargs):
        directions = ["up", "down", "left", "right", "stop"]

        # check distance to player

        self.distance_to_player = self.world_map.check_distance_to_player(self.y, self.x)
        print(self.distance_to_player)

        if self.distance_to_player < 12:
            chosen_dir = self.chase_player(directions)
        else:
            chosen_dir = random.choice(directions)
            # chosen_dir = "stop"

        # chosen_dir = random.choice(directions)
        # chosen_dir = "stop"
        self.move(chosen_dir)


class Goblin(Character):
    def __init__(self, y, x, world_map, game_instance):
        super().__init__(y, x, world_map, game_instance)
        self.glyph = "G"
        self.glyph_color = "Green"
        self.glyph_inverted = True
        self.action_points = random.randint(3, 5)
        global goblin_names
        self.short_name = random.choice(goblin_names)
        self.name = self.short_name + " Goblin"
        self.endurance = random.randint(14, 18)
        self.health = random.randint(12, 16)
        self.melee_skill = random.randint(26, 34)
        self.distance_to_player = 255
        self.update_stats()
        self.EXP_value = 45
        self.on_create()

    def update(self, *args, **kwargs):
        directions = ["up", "down", "left", "right", "stop", "stop", "stop"]

        # check distance to player

        self.distance_to_player = self.world_map.check_distance_to_player(self.y, self.x)
        print(self.distance_to_player)

        if self.distance_to_player < 12:
            chosen_dir = self.chase_player(directions)
        else:
            chosen_dir = random.choice(directions)
            # chosen_dir = "stop"

        # chosen_dir = random.choice(directions)
        # chosen_dir = "stop"
        self.move(chosen_dir)
