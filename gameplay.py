from __future__ import annotations
import game_control
import map_loader
import player
import mobs
import random
import curses
import pickables
import world_static
import ui
import combat
import map_populator


class GameInstance(game_control.Scene):
    """
    Game Instance - object for playthrough of a level
    """

    def __init__(self, windows, name: str, engine: object, character_sheet):
        super().__init__(windows, name, engine)
        self.character_sheet = character_sheet
        self.UI_window = self.windows[-1]  # window for UI data
        self.GP_window = self.windows[0]  # Gameplay window - map and player
        self.mobs = []
        self.grid = None
        self.current_player = None
        self.load_map("Test_map_1")

    def load_map(self, map_name: "str"):
        """
        This loads map and sets reference in game instance
        """
        self.grid = map_loader.WorldMap(map_name, self.character_sheet["current_map"])
        self.current_player = player.Player(self.grid.player_y,
                                            self.grid.player_x,
                                            self.character_sheet,
                                            self.grid,
                                            self)
        self.grid.grid[self.grid.player_y][self.grid.player_x].occupation = self.current_player

        grid_map = SituationMap(self.GP_window, self.grid, self)
        self.renderable_objects.append(grid_map)
        character_info = CharacterSheet(self.UI_window, self)
        self.renderable_objects.append(character_info)
        self.secondary_update.append(self.current_player)
        self.updatable_objects.append(character_info)
        self.secondary_update.append(self)

        # test_mobs
        population = map_populator.level_contents(self.current_player.current_map)
        population_names = map_populator.population_dictionary()
        print(population)

        for item in population['creatures']:
            for i in range(population['creatures'][item]):
                available_cells = self.grid.get_available_spaces()
                coord = random.choice(available_cells)
                created_mob = population_names[item](coord[0], coord[1], self.grid, self)
                self.mobs.append(created_mob)
                self.grid.grid[coord[0]][coord[1]].occupation = created_mob
                self.updatable_objects.append(created_mob)

        for item in population['pickables']:
            for i in range(population['pickables'][item]):
                available_cells = self.grid.get_available_spaces()
                coord = random.choice(available_cells)
                created_item = population_names[item]()
                self.grid.grid[coord[0]][coord[1]].pickable = created_item

    def ask_Dump_or_Equip(self, key):
        scene = DumpOrEquip([self.engine.popup_screen], "Dump or Equip?", self.engine, self, self.current_player, key)
        self.engine.change_scene(scene)

    def update(self, key):
        self.dijkstra_map()

    def check_neighbours(self, enemies=True):
        if enemies:
            # directions
            up = [self.grid.player_y - 1, self.grid.player_x]
            down = [self.grid.player_y + 1, self.grid.player_x]
            left = [self.grid.player_y, self.grid.player_x - 1]
            right = [self.grid.player_y, self.grid.player_x + 1]

            found_enemies = []

            if isinstance(self.grid.grid[up[0]][up[1]].occupation, player.Character):
                found_enemies.append(self.grid.grid[up[0]][up[1]].occupation)
            elif isinstance(self.grid.grid[down[0]][down[1]].occupation, player.Character):
                found_enemies.append(self.grid.grid[down[0]][down[1]].occupation)
            elif isinstance(self.grid.grid[left[0]][left[1]].occupation, player.Character):
                found_enemies.append(self.grid.grid[left[0]][left[1]].occupation)
            elif isinstance(self.grid.grid[right[0]][right[1]].occupation, player.Character):
                found_enemies.append(self.grid.grid[right[0]][right[1]].occupation)
            else:
                pass

            if len(found_enemies) > 0:
                new_combat_screen = combat.CombatScreen([self.engine.full_screen], "Combat Screen", self.engine,
                                                        self, self.current_player, found_enemies[0])
                self.engine.change_scene(new_combat_screen)
            else:
                pass
        else:
            pass

    def dijkstra_map(self):

        # reset grid

        for y in range(len(self.grid.grid)):
            for x in range(len(self.grid.grid[y])):
                self.grid.grid[y][x].distance_to_player = 255

        curpos_y = self.grid.player_y
        curpos_x = self.grid.player_x

        self.grid.grid[curpos_y][curpos_x].distance_to_player = 0

        neighbours = [self.grid.grid[curpos_y][curpos_x]]
        future_neighbours = []
        iteration = 0

        while iteration < 244 and len(neighbours) > 0:
            for cell in neighbours:
                cell.distance_to_player = iteration
                # collect neighbours
                north = self.grid.grid[cell.y - 1][cell.x]
                if (north.occupation == "free" or isinstance(north.occupation,
                                                             player.Character)) and north.distance_to_player == 255 and north not in future_neighbours:
                    future_neighbours.append(north)
                south = self.grid.grid[cell.y + 1][cell.x]
                if (south.occupation == "free" or isinstance(south.occupation,
                                                             player.Character)) and south.distance_to_player == 255 and south not in future_neighbours:
                    future_neighbours.append(south)
                west = self.grid.grid[cell.y][cell.x - 1]
                if (west.occupation == "free" or isinstance(west.occupation,
                                                            player.Character)) and west.distance_to_player == 255 and west not in future_neighbours:
                    future_neighbours.append(west)
                east = self.grid.grid[cell.y][cell.x + 1]
                if (east.occupation == "free" or isinstance(east.occupation,
                                                            player.Character)) and east.distance_to_player == 255 and east not in future_neighbours:
                    future_neighbours.append(east)

            neighbours = future_neighbours
            future_neighbours = []
            iteration += 1


class CharacterSheet:
    """
    UI info in the left window
    """

    def __init__(self, window, game_instance: GameInstance):
        self.window = window
        self.window_y, self.window_x = window.getmaxyx()
        self.game_instance = game_instance

    def draw(self, inventory=True):
        min_y = 1
        max_y = self.window_y - 1
        min_x = 1
        max_x = self.window_x - 1
        center_y = int(self.window_y / 2)
        center_x = int(self.window_x / 2)

        self.window.addstr(min_y, center_x - 3, "Hp:" + str(self.game_instance.current_player.current_health) + "/" +
                           str(self.game_instance.current_player.health))
        self.window.addstr(2, min_x, "Mel:" + str(self.game_instance.current_player.melee_skill))
        self.window.addstr(2, max_x - len("AP:" + str(self.game_instance.current_player.action_points)),
                           "AP:" + str(self.game_instance.current_player.action_points))
        self.window.addstr(3, min_x, "Str:" + str(self.game_instance.current_player.strengh))
        self.window.addstr(3, max_x - len("End:" + str(self.game_instance.current_player.endurance)),
                           "End:" + str(self.game_instance.current_player.endurance))

        # Weapon and armour
        self.window.addstr(4,
                           int(center_x - len("Head:[" + str(self.game_instance.current_player.arm_head) + "]") / 2),
                           "Head:[" + str(self.game_instance.current_player.arm_head) + "]")
        self.window.addstr(5,
                           int(center_x - len("Torso:[" + str(self.game_instance.current_player.arm_torso) + "]") / 2),
                           "Torso:[" + str(self.game_instance.current_player.arm_torso) + "]")
        self.window.addstr(6,
                           int(center_x - len("Hands:[" + str(self.game_instance.current_player.arm_hands) + "]") / 2),
                           "Hands:[" + str(self.game_instance.current_player.arm_hands) + "]")
        self.window.addstr(7,
                           int(center_x - len("Legs:[" + str(self.game_instance.current_player.arm_legs) + "]") / 2),
                           "Legs:[" + str(self.game_instance.current_player.arm_legs) + "]")

        self.window.addstr(9,
                           int(center_x - len("Weapon:[" + str(self.game_instance.current_player.weapon) + "]") / 2),
                           "Weapon:[" + str(self.game_instance.current_player.weapon) + "]")

        # Inventory
        if inventory:
            self.window.addstr(10, min_x, "Inventory:")

            self.window.addstr(11, min_x, "1:[" + str(self.game_instance.current_player.inv_1) + "]")

            self.window.addstr(11, max_x - (len("2:[" + str(self.game_instance.current_player.inv_2) + "]")),
                               "2:[" + str(self.game_instance.current_player.inv_2) + "]")

            self.window.addstr(12, min_x, "3:[" + str(self.game_instance.current_player.inv_3) + "]")

            self.window.addstr(12, max_x - (len("4:[" + str(self.game_instance.current_player.inv_4) + "]")),
                               "4:[" + str(self.game_instance.current_player.inv_4) + "]")

    def update(self, key):
        self.draw(True)


class SituationMap:
    """
    This is object responsible for drawing main gameplay window
    """

    def __init__(self, window, grid, game_instance: GameInstance):
        self.window = window
        self.grid = grid
        self.window_y, self.window_x = window.getmaxyx()
        self.game_instance = game_instance
        self.colors = {False:
                           {"Red": curses.color_pair(4),
                            "White": curses.color_pair(6),
                            "Yellow": curses.color_pair(1),
                            "Blue": curses.color_pair(3),
                            "Magenta": curses.color_pair(5),
                            "Green": curses.color_pair(7)},
                       True:
                           {"Yellow": curses.color_pair(2),
                            "White": curses.color_pair(21),
                            "Red": curses.color_pair(24),
                            "Magenta": curses.color_pair(23),
                            "Blue": curses.color_pair(22),
                            "Green": curses.color_pair(25),
                            }
                       }

    def draw(self):
        """
        this method is required in all object that are
        to be addet to renderable list of the scene
        """
        min_y = 1
        max_y = self.window_y - 1
        min_x = 1
        max_x = self.window_x - 1
        center_y = int(self.window_y / 2)
        center_x = int(self.window_x / 2)

        # get beginning
        diff_y = self.grid.player_y - center_y
        diff_x = self.grid.player_x - center_x

        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                if 0 < y + diff_y < len(self.grid.grid) and 0 < x + diff_x < len(self.grid.grid[0]):
                    if isinstance(self.grid.grid[y + diff_y][x + diff_x].occupation, player.Character):
                        char = self.grid.grid[y + diff_y][x + diff_x].occupation
                        self.window.addstr(y, x, str(self.grid.grid[y + diff_y][x + diff_x]),
                                           self.colors[char.glyph_inverted][char.glyph_color])
                    elif isinstance(self.grid.grid[y + diff_y][x + diff_x].occupation, world_static.LevelEnd):
                        char = self.grid.grid[y + diff_y][x + diff_x].occupation
                        self.window.addstr(y, x, str(self.grid.grid[y + diff_y][x + diff_x]),
                                           self.colors[char.glyph_inverted][char.glyph_color])
                    elif isinstance(self.grid.grid[y + diff_y][x + diff_x].pickable, world_static.Pickable):
                        char = self.grid.grid[y + diff_y][x + diff_x].pickable
                        self.window.addstr(y, x, str(self.grid.grid[y + diff_y][x + diff_x]),
                                           self.colors[char.glyph_inverted][char.glyph_color])
                    else:
                        self.window.addstr(y, x, str(self.grid.grid[y + diff_y][x + diff_x]))
                else:
                    self.window.addstr(y, x, "#")

                    # draw static map elements first, then dynamic objects like player

        # self.window.addstr(center_y, center_x, self.game_instance.current_player.glyph)


class DumpOrEquip(game_control.Scene):
    def __init__(self, windows, name: str, engine: object, escape: GameInstance, current_player, key):
        super().__init__(windows, name, engine)
        self.current_player = current_player
        self.item_slot = key
        self.escape = escape
        self.center_y = int(self.win_y / 2)
        self.center_x = int(self.win_x / 2)
        self.updatable_objects.append(self)
        self.button_names = ["EQUIP", "DUMP"]
        self.buttons_on_pressed = {
            "EQUIP": [self.equip, []],
            "DUMP": [self.dump, []],
        }
        self.print_content()

    def print_content(self):
        obj_in_question = self.current_player.get_inventory_state(self.item_slot)
        relevant_char = {"weapon": "Attack: " + str(obj_in_question.strenght),
                         "arm_head": "Defence: " + str(obj_in_question.defence_points),
                         "arm_torso": "Defence: " + str(obj_in_question.defence_points),
                         "arm_hands": "Defence: " + str(obj_in_question.defence_points),
                         "arm_legs": "Defence: " + str(obj_in_question.defence_points),
                         "consumable": "Health: +" + str(obj_in_question.health),
                         }
        main_label = \
            "[" + obj_in_question.name + "] " + relevant_char[obj_in_question.destination]

        self.renderable_objects.append(ui.Label(self.windows[0],
                                                main_label,
                                                2,
                                                self.center_x - (int(len(main_label) / 2)),
                                                bg="white")
                                       )
        for num, button in enumerate(self.button_names):
            self.menu_buttons.append(ui.button(self.windows[0],
                                               2 + 1 + num,
                                               self.center_x - (int(len(button) / 2)),
                                               button,
                                               button,
                                               self.buttons_on_pressed[button][0],
                                               self.buttons_on_pressed[button][1]))

        for button in self.menu_buttons:
            self.renderable_objects.append(button)

        self.menu_buttons[self.focused_item].is_focused = True

    def update(self, key):
        self.button_toggle(key)

    def dump(self):
        if self.escape.grid.grid[self.current_player.y][self.current_player.x].pickable == "free":
            self.escape.grid.grid[self.current_player.y][self.current_player.x].pickable = \
                self.current_player.get_inventory_state(self.item_slot)
            self.current_player.set_inventory_state(self.item_slot, None)
        else:
            item_to_swap = self.escape.grid.grid[self.current_player.y][self.current_player.x].pickable
            self.escape.grid.grid[self.current_player.y][self.current_player.x].pickable = \
                self.current_player.get_inventory_state(self.item_slot)
            self.current_player.set_inventory_state(self.item_slot, item_to_swap)

        self.engine.change_scene(self.escape)

    def equip(self):
        item = self.current_player.get_inventory_state(self.item_slot)
        bodypart = self.current_player.get_inventory_state(self.item_slot).destination
        if self.current_player.get_bodypart_state(item.destination) is None:
            self.current_player.set_bodypart_state(bodypart, item)
        else:
            item_to_swap = self.current_player.get_bodypart_state(item.destination)
            self.current_player.set_bodypart_state(bodypart, item)
            self.current_player.set_inventory_state(self.item_slot, item_to_swap)

        self.engine.change_scene(self.escape)
