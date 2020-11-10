# Data with populate information and balancing
import pickables
import mobs


def level_contents(map_no: int):
    content = {1: {"creatures": {"Rat": 12,
                                 "Rat_Warrior": 4,
                                 "Goblin": 2,
                                 },
                   "pickables": {"Dagger": 2,
                                 "Mace": 4,
                                 },
                   },

               2: {"creatures": {"Rat": 18,
                                 "Rat_Warrior": 8,
                                 "Goblin": 4,
                                 },
                   "pickables": {"Dagger": 3,
                                 "Mace": 5,
                                 },
                   },
               3: {"creatures": {"Rat": 18,
                                 "Rat_Warrior": 8,
                                 "Goblin": 8,
                                 },
                   "pickables": {"Dagger": 3,
                                 "Mace": 5,
                                 },
                   }
               }

    return content[map_no]


def population_dictionary():
    dictionary = {"Rat": mobs.Rat,
                  "Rat_Warrior": mobs.RatWarrior,
                  "Goblin": mobs.Goblin,
                  "Dagger": pickables.Dagger,
                  "Mace": pickables.Mace,
                  }
    return dictionary
