
def load_map(map_name):
    grid = []
    map = open('resources/maps/' + map_name, 'r')

    for line in map:
        grid.append(list(line.rstrip("\n")))

    for y in range (1, len(grid)-1):
        for x in range(1, len(grid[y])-1):
            if grid[y][x] == "/":
                grid[y][x]="█"
            if grid[y][x]=="@" and (grid[y][x+1] == " " or grid[y][x-1]==" " or grid[y-1][x]==" " or grid[y+1][x]==" "):
                grid[y][x] = "█"



    for row in grid:
        print("".join(row))

if __name__ == '__main__':
    load_map('Test_map_1')
    input()