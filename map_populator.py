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
                                 "HealingRay": 2,
                                 },
                   },

               2: {"creatures": {"Rat": 18,
                                 "Rat_Warrior": 8,
                                 "Goblin": 4,
                                 },
                   "pickables": {"Dagger": 3,
                                 "Mace": 5,
                                 "Helmet": 2,
                                 "HealthPotion": 3,
                                 "Fireball": 6,
                                 "HealingRay": 2
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
                                 "Fireball": 6,
                                 "HealingRay": 6,
                                 "HealthDrain": 6,
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
                  "HealingRay": cards.HealingRay,
                  "HealthDrain": cards.HealthDrain,
                  "Poison": cards.Poison,
                  "PoisonedBlade": cards.PoisonedBlade,
                  "FullRecover": cards.FullRecover,
                  "PoisonousCloud": cards.PoisonousCloud,
                  "SacrificeKill": cards.SacrificeKill,
                  }
    return dictionary
