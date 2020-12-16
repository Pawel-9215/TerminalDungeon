# Data with populate information and balancing
import pickables
import cards
import mobs


def level_contents(map_no: int):
    content = {1: {"creatures": {"Rat": 12,
                                 "Rat_Warrior": 4,
                                 "Goblin": 2,
                                 },
                   "pickables": {"Dagger": 2,
                                 "Mace": 4,
                                 "Helmet": 2,
                                 "HealthPotion": 1,
                                 },
                   },

               2: {"creatures": {"Rat": 18,
                                 "Rat_Warrior": 8,
                                 "Goblin": 4,
                                 },
                   "pickables": {"Dagger": 3,
                                 "Mace": 5,
                                 "Helmet": 2,
                                 "HealthPotion": 3
                                 "Fireball": 2,
                                 },
                   },
               3: {"creatures": {"Rat": 18,
                                 "Rat_Warrior": 8,
                                 "Goblin": 8,
                                 },
                   "pickables": {"Dagger": 3,
                                 "Mace": 5,
                                 "Helmet": 3,
                                 "HealthPotion": 4,
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
                  "Helmet": pickables.Helmet,
                  "HealthPotion": pickables.HealthPotion,
                  "Fireball": cards.Fireball,
                  }
    return dictionary
