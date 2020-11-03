# Data with populate information and balancing

def level_contents(map_no: int):

    content = {1: {"Rat": 12,
                   "Rat_Warrior": 4,
                   "Goblin": 2,
                   "Dagger": 2,
                   "Mace": 4,
                   },
               2: {"Rat": 16,
                   "Rat_Warrior": 8,
                   "Goblin": 4,
                   "Dagger": 4,
                   "Mace": 5,
                   },
               }

    return content[map_no]
