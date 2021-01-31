# This is place to add items for player to pick
import random
from world_static import Pickable


class TorsoArmour(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "A"
        self.glyph_inverted = False
        self.glyph_color = "Blue"
        self.name = "Armour"
        self.destination = "arm_torso"
        self.defence_points = random.randint(1, 2)


class HandArmour(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "A"
        self.glyph_inverted = False
        self.glyph_color = "Magenta"
        self.name = "Armour"
        self.destination = "arm_hands"
        self.defence_points = random.randint(1, 2)


class LegArmour(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "A"
        self.glyph_inverted = False
        self.glyph_color = "White"
        self.name = "Armour"
        self.destination = "arm_legs"
        self.defence_points = random.randint(1, 2)


class Weapon(Pickable):
    def __init__(self):
        super().__init__()
        self.destination = "weapon"
        self.glyph = "W"
        self.glyph_inverted = True
        self.glyph_color = "Yellow"
        self.name = "Dagger"
        self.strenght = (1, 2)


class Dagger(Weapon):
    def __init__(self):
        super().__init__()
        self.glyph = "W"
        self.glyph_inverted = True
        self.glyph_color = "Yellow"
        self.name = "Dagger"
        self.strenght = (1, 2)


class Mace(Weapon):
    def __init__(self):
        super().__init__()
        self.glyph = "W"
        self.glyph_inverted = True
        self.glyph_color = "Magenta"
        self.name = "Mace"
        self.strenght = (0, 2)


class HealthPotion(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "H"
        self.glyph_inverted = True
        self.glyph_color = "Red"
        self.name = "HealthPotion"
        self.consumable = True


class Helmet(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "A"
        self.glyph_inverted = False
        self.glyph_color = "Yellow"
        self.name = "Helmet"
        self.destination = "arm_head"
        self.defence_points = random.randint(3, 5)


class LeatherJacket(Pickable):
    def __init__(self):
        super().__init__()
        self.glyph = "A"
        self.glyph_inverted = False
        self.glyph_color = "Green"
        self.name = "Leather Jacket"
        self.destination = "arm_torso"
        self.defence_points = random.randint(1, 2)


class StuddedJacket(TorsoArmour):
    def __init__(self):
        super().__init__()
        self.name = "Studded Jacket"
        self.defence_points = random.randint(2, 3)


class ChainMail(TorsoArmour):
    def __init__(self):
        super().__init__()
        self.name = "Chain Mail"
        self.defence_points = random.randint(3, 5)


class PlateArmour(TorsoArmour):
    def __init__(self):
        super().__init__()
        self.name = "Plate Armour"
        self.defence_points = random.randint(5, 8)


class LeatherCap(Helmet):
    def __init__(self):
        super().__init__()
        self.name = "Leather Cap"
        self.defence_points = random.randint(1, 1)


class ChainMailHood(Helmet):
    def __init__(self):
        super().__init__()
        self.name = "Chain Mail Hood"
        self.defence_points = random.randint(2, 3)


class LeatherGloves(HandArmour):
    def __init__(self):
        super().__init__()
        self.name = "Leather gloves"
        self.defence_points = random.randint(0, 1)


class ChainMailGloves(HandArmour):
    def __init__(self):
        super().__init__()
        self.name = "Chainmail gloves"
        self.defence_points = random.randint(2, 3)


class PlateGloves(HandArmour):
    def __init__(self):
        super().__init__()
        self.name = "Plate gloves"
        self.defence_points = random.randint(2, 4)


class LeatherBoots(LegArmour):
    def __init__(self):
        super().__init__()
        self.name = "Leather Boots"
        self.defence_points = random.randint(1, 2)


class ReinforcedLeatherBoots(LegArmour):
    def __init__(self):
        super().__init__()
        self.name = " ReinforcedLeather Boots"
        self.defence_points = random.randint(2, 3)


class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.glyph_color = "White"
        self.name = "Sword"
        self.strenght = (3, 5)


class Axe(Weapon):
    def __init__(self):
        super().__init__()
        self.glyph_color = "White"
        self.name = "Axe"
        self.strenght = (3, 6)


class RustySword(Weapon):
    def __init__(self):
        super().__init__()
        self.glyph_color = "Red"
        self.name = "Rusty Sword"
        self.strenght = (2, 3)


class Morgenstern(Weapon):
    def __init__(self):
        super().__init__()
        self.glyph_color = "Yellow"
        self.name = "Morgenstern"
        self.strenght = (4, 5)


class DwarvenAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.glyph_color = "Red"
        self.name = "Rvwarven Axe"
        self.strenght = (6, 7)


class ElvishBlade(Weapon):
    def __init__(self):
        super().__init__()
        self.glyph_color = "Blue"
        self.name = "Elvish Blade"
        self.strenght = (5, 9)


class ScynthianSword(Weapon):
    def __init__(self):
        super().__init__()
        self.glyph_color = "Magenta"
        self.name = "Scynthian Sword"
        self.strenght = (10, 12)