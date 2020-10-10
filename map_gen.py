import random


# test_map = open('resources/maps/test_map2', 'w+')


def generate_map(y_s, x_s):
    game_map = []

    for y in range(y_s):
        game_map.append([" "] * x_s)

    for y in range(y_s):
        for x in range(x_s):
            game_map[y][x] = "@"

    # vertical variant

    x_margin = round(x_s / 12)
    x_start = random.randint(0 + x_margin, x_s - x_margin)
    y_margin = round(y_s / 12)
    y_start = y_s - y_margin
    iterations = round(x_s / 10)

    current_cell = [y_start, x_start]
    # game_map[current_cell[0]][current_cell[1]] = " "

    for i in range(iterations):
        current_cell = [y_start, x_start]
        while current_cell[0] > y_margin:

            game_map[current_cell[0]][current_cell[1]] = " "
            last_direction = "left"

            if random.randint(1, 3) == 2:
                go = "up"
            elif random.randint(1, 2 + i) == 3 and (x_margin < current_cell[1] or current_cell[1] < x_s - x_margin):
                go = last_direction
            elif 3 * x_margin > current_cell[1] or current_cell[1] > x_s - x_margin * 3:
                if random.randint(1, 99) <= ((current_cell[1] - x_margin) / (x_s - (2 * x_margin))) * 100:
                    go = "left"
                else:
                    go = "right"
            else:
                go = random.choice(["left", "right"])

            if go == "up":
                current_cell[0] -= 1
                last_direction = "up"
            elif go == "left":
                current_cell[1] -= 1
                last_direction = "left"
            else:
                current_cell[1] += 1
                last_direction = "right"

    for row in game_map:
        print("".join(row))


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

    for i in range(steps):
        game_map = simulation_step(game_map)

    for row in game_map:
        print("".join(row))


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


y_size = int(input("Give Y: "))
x_size = int(input("Give X: "))
chance_alive = int(input("Fill percent: "))

generate_map_ca(y_size, x_size, chance_alive)

_ = input()
