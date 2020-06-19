import random
import world_static


def load_map(map_name):
    grid = []
    map = open('resources/maps/' + map_name, 'r')
    floor = [" ", ",", ".", " ", " ", ",", " ", " ", " "]
    player_yx = []
    for line in map:
        grid.append(list(line.rstrip("\n")))

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if grid[y][x] == "/":
                grid[y][x] = "█"
            if grid[y][x] == "@" and (
                    grid[y][x + 1] == " " or grid[y][x - 1] == " " or grid[y - 1][x] == " " or grid[y + 1][x] == " "):
                grid[y][x] = "█"
            if grid[y][x] == "P":
                player_yx = [x, y]
                grid[y][x] = "P"
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if grid[y][x] == " ":
                grid[y][x] = " "

    return grid


"""
    for row in grid:
        print("".join(row))
"""


def populate_map(map_name):
    floor = [" ", ",", ".", " ", " ", ",", " ", " ", " "]
    objects = {
        "@":world_static.Cell(random.choice(floor), occupation=world_static.Rock),
        "█":world_static.Cell(random.choice(floor), occupation=world_static.StoneWall),
        " ":world_static.Cell(random.choice(floor), occupation="free")
    }

    base_grid = load_map(map_name)
    populated_grid = []

    for y in range(base_grid):
        for x in range(base_grid[x]):
            pass




if __name__ == '__main__':
    map = load_map('Test_map_1')
    for row in map:
        print("".join(row))
    input()
