import random


# test_map = open('resources/maps/test_map2', 'w+')


def generate_map(game_map):
    """
    game_map = []

    for y in range(y_s):
        game_map.append([" "] * x_s)

    for y in range(y_s):
        for x in range(x_s):
            game_map[y][x] = "@"
    """
    y_s = len(game_map)
    x_s = len(game_map[0])
    # vertical variant

    x_margin = round(x_s / 10)
    x_start = random.choice([random.randint(0 + x_margin, x_s / 2 - 2 * x_margin),
                             random.randint(x_s / 2 + 2 * x_margin, x_s - x_margin)])
    y_margin = round(y_s / 12)
    y_start = y_s - y_margin
    iterations = 2
    if x_start < x_s / 2:
        start_dir = "left"
    else:
        start_dir = "right"
    print(start_dir)
    current_cell = [y_start, x_start]

    # game_map[current_cell[0]][current_cell[1]] = " "

    for _ in range(iterations):
        current_cell = [y_start, x_start]
        while current_cell[0] > y_margin:

            game_map[current_cell[0]][current_cell[1]] = " "
            last_direction = "left"

            if random.randint(1, 3) == 2:
                go = "up"

            elif start_dir == "left":
                if random.randint(0, 100) <= (
                        (current_cell[1] - round(x_margin + x_s / 2)) / (x_s - round(x_s / 2 + x_margin))) * 100:
                    go = "left"
                else:
                    go = "right"

            elif start_dir == "right":
                if random.randint(0, 100) <= ((current_cell[1]) / (round(x_s / 2) - x_margin)) * 100:
                    go = "left"
                else:
                    go = "right"

            else:
                go = last_direction

            if go == "up":
                current_cell[0] -= 1
                last_direction = "up"
            elif go == "left":
                current_cell[1] -= 1
                last_direction = "left"
            else:
                current_cell[1] += 1
                last_direction = "right"

    traversal = random.choice(["top", "down"])
    if traversal == "top":
        game_map[current_cell[0]][current_cell[1]] = "E"
        current_cell = [y_start, x_start]
        game_map[current_cell[0]][current_cell[1]] = "P"
    else:
        game_map[current_cell[0]][current_cell[1]] = "P"
        current_cell = [y_start, x_start]
        game_map[current_cell[0]][current_cell[1]] = "E"

    return game_map


def generate_map_ca(y_s, x_s, alive_chance=45, steps=1):
    game_map = []

    for y in range(y_s):
        game_map.append([" "] * x_s)

    for y in range(y_s):
        for x in range(x_s):
            roll = random.randint(0, 100)
            if roll <= alive_chance:
                game_map[y][x] = "@"
            else:
                game_map[y][x] = " "

    for _ in range(steps):
        game_map = simulation_step(game_map)

    game_map = generate_map(game_map)

    for y in range(len(game_map)):
        for x in range(len(game_map[y])):
            if y in [0, 1] or y == len(game_map)-1:
                game_map[y][x] = "@"
            if x in [0, 1] or x == len(game_map[y])-1:
                game_map[y][x] = "@"

    for row in game_map:
        print("".join(row))

    return game_map


def simulation_step(game_map):
    new_map = game_map

    birth_limit = 4
    death_limit = 3

    for y in range(0, len(game_map) - 1):
        for x in range(0, len(game_map[y]) - 1):
            neighboburs = [game_map[y - 1][x - 1],
                           game_map[y - 1][x],
                           game_map[y - 1][x + 1],
                           game_map[y][x - 1],
                           game_map[y][x + 1],
                           game_map[y + 1][x - 1],
                           game_map[y + 1][x],
                           game_map[y + 1][x + 1],
                           ]
            alive_count = neighboburs.count("@")
            if game_map[y][x] == "@" and alive_count < death_limit:
                new_map[y][x] = " "
            elif game_map[y][x] == " " and alive_count > birth_limit:
                new_map[y][x] = "@"

    return new_map


if __name__ == '__main__':
    y_size = int(input("Give Y: "))
    x_size = int(input("Give X: "))
    chance_alive = int(input("Fill percent: "))

    # generate_map_ca(y_size, x_size, chance_alive)
    tester = "r"
    while tester != "f":
        generate_map_ca(y_size, x_size, chance_alive)
        tester = input()
