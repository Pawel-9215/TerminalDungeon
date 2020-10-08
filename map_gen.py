import random


# test_map = open('resources/maps/test_map2', 'w+')


def generate_map(y_s, x_s):
    game_map = []

    for y in range(y_s):
        game_map.append([" "]*x_s)

    for y in range(y_s):
        for x in range(x_s):
            game_map[y][x] = "@"

    # vertical variant

    x_margin = round(x_s/6)
    x_start = random.randint(0+x_margin, x_s - x_margin)
    y_margin = round(y_s/8)
    y_start = y_s - y_margin
    iterations = round(x_s/10)

    current_cell = [y_start, x_start]
    print(current_cell[0])
    print(current_cell[1])
    # game_map[current_cell[0]][current_cell[1]] = " "

    for i in range(iterations):
        current_cell = [y_start, x_start]
        while current_cell[0] > y_margin:

            game_map[current_cell[0]][current_cell[1]] = " "

            if random.randint(1, 3) == 1:
                go = "up"
            else:
                if random.randint(1, 99) <= ((current_cell[1]-x_margin)/(x_s-(2*x_margin)))*100:
                    go = "left"
                else:
                    go = "right"

            if go == "up":
                current_cell[0] -= 1
            elif go == "left":
                current_cell[1] -= 1
            else:
                current_cell[1] += 1

    for row in game_map:
        print("".join(row))


y_size = int(input("Give Y: "))
x_size = int(input("Give X: "))

generate_map(y_size, x_size)

_ = input()
