import random
import world_static


class WorldMap():
    """
    This is world map object. This is where grid lives,
    this is object to ask what's around us,
    this is the object that let's us go forward.
    Respect this object
    """
    def __init__(self, map_name: str):
        self.player_y = 0
        self.player_x = 0
        self.map_name = map_name
        self.grid = self.populate_map()

    def load_map(self):
        """
        This methon first interpret text based map to clean list object
        """

        grid = []
        map = open('resources/maps/' + self.map_name, 'r')

        for line in map:
            grid.append(list(line.rstrip("\n")))

        for y in range(1, len(grid) - 1):
            for x in range(1, len(grid[y]) - 1):
                if grid[y][x] == "/":
                    grid[y][x] = "█"
                if grid[y][x] == "@" and (
                        grid[y][x + 1] == " " or grid[y][x - 1] == " " or grid[y - 1][x] == " " or grid[y + 1][
                    x] == " "):
                    grid[y][x] = "█"
                if grid[y][x] == "P":
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
                    "@": world_static.Cell(current_floor, occupation=world_static.Rock()),
                    "█": world_static.Cell(current_floor, occupation=world_static.StoneWall()),
                    " ": world_static.Cell(current_floor),
                    "P": world_static.Cell(current_floor,
                                           occupation=world_static.PlayerStart(self.player_y, self.player_x)),
                }
                base_grid[y][x] = objects[base_grid[y][x]]

        return base_grid


if __name__ == '__main__':
    my_map = WorldMap('Test_map_1')
    map = my_map.load_map()
    for row in map:
        print("".join(row))

    print(my_map.grid)
    input()
