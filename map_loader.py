from __future__ import annotations
import random
import world_static
import map_gen
import game_control
import ui


class WorldMap:
    """
    This is world map object. This is where grid lives,
    this is object to ask what's around us,
    this is the object that let's us go forward.
    Respect this object.
    """

    def __init__(self, map_name: str, current_map: int):
        self.player_y = 0
        self.player_x = 0
        self.map_name = map_name
        self.current_map = current_map
        self.grid = self.populate_map()

    def load_map(self):
        """
        This methon first interpret text based map to clean list object
        """
        map_y = (1 + round(self.current_map / 10)) * 50
        map_x = (1 + round(self.current_map / 10)) * 90
        grid = map_gen.generate_map_ca(map_y, map_x, 42, 2)
        '''
        dungeon_map = open('resources/maps/' + self.map_name, 'r')

        for line in dungeon_map:
            grid.append(list(line.rstrip("\n")))
        '''
        for y in range(1, len(grid) - 1):
            for x in range(1, len(grid[y]) - 1):
                if grid[y][x] == "/":
                    grid[y][x] = "█"
                elif grid[y][x] == "@" and (
                        grid[y][x + 1] == " " or grid[y][x - 1] == " " or grid[y - 1][x] == " " or grid[y + 1][
                    x] == " "):
                    grid[y][x] = "█"
                elif grid[y][x] == "P":
                    self.player_y = y
                    self.player_x = x

        for y in range(1, len(grid) - 1):
            for x in range(1, len(grid[y]) - 1):
                if grid[y][x] == " ":
                    grid[y][x] = " "

        return grid

    def populate_map(self):
        """
        Now this method reinterptret string based map to object based
        two dimensional list
        """

        floor = [" ", ",", ".", " ", " ", ",", " ", " ", " "]

        base_grid = self.load_map()

        for y in range(len(base_grid)):
            for x in range(len(base_grid[y])):
                current_floor = random.choice(floor)
                objects = {
                    "@": world_static.Cell(current_floor, y, x, occupation=world_static.Rock()),
                    "█": world_static.Cell(current_floor, y, x, occupation=world_static.StoneWall()),
                    " ": world_static.Cell(current_floor, y, x),
                    "E": world_static.Cell(current_floor, y, x, pickable=world_static.LevelEnd(y, x)),
                    "P": world_static.Cell(current_floor, y, x,
                                           occupation=world_static.PlayerStart(self.player_y, self.player_x)),
                }
                base_grid[y][x] = objects[base_grid[y][x]]

        return base_grid

    def check_content(self, y, x):

        return self.grid[y][x].occupation

    def check_distance_to_player(self, y, x):

        return self.grid[y][x].distance_to_player

    def get_available_spaces(self):

        available_spaces = []

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x].occupation == "free":
                    available_spaces.append((y, x))

        return available_spaces


class New_level(game_control.Scene):
    """
    Scene that shows up between levels
    """

    def __init__(self, windows, name: str, engine: object, character_sheet, player):
        super().__init__(windows, name, engine)
        self.character_sheet = character_sheet
        self.current_player = player
        self.window_y, self.window_x = windows[0].getmaxyx()
        self.draw_content()

    def draw_content(self):
        center_x = int(self.window_x / 2)
        min_y = 2

        line1 = "You are descending further into the caves"
        line2 = "You are entering level "+str(self.character_sheet["current_map"]+1)

        info1 = ui.Plain_text(self.windows[0],
                              line1,
                              min_y,
                              center_x - round(len(line1) / 2)
                              )

        info2 = ui.Plain_text(self.windows[0],
                              line2,
                              min_y+1,
                              center_x - round(len(line2) / 2)
                              )

        self.renderable_objects.append(info1)
        self.renderable_objects.append(info2)

        pass

    def update_character_sheet(self):
        pass

    def start_new_level(self):
        pass
