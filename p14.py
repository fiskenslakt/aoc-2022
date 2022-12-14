from aocd import lines, submit

# lines = '''498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9'''.splitlines()
SAND_SOURCE = (500, 0)


def display_cave():
    for y in range(max_y+1):
        for x in range(min_x, max_x+1):
            if x == 500 and y == 0:
                print('+', end='')
            elif (x,y) in cave:
                print(cave[(x,y)], end='')
            else:
                print('.', end='')
        print()


cave = {}
min_x = float('inf')
max_x = 0
max_y = 0
# build the cave
for line in lines:
    coords = line.split(' -> ')
    lx, ly = None, None
    for coord in coords:
        x, y = map(int, coord.split(','))
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        if lx is not None:
            sx, bx = sorted((lx, x))
            sy, by = sorted((ly, y))
            for i in range(sx, bx+1):
                for j in range(sy, by+1):
                    cave[(i, j)] = '#'
        lx, ly = x, y

# simulate sand
resting_sand = 0
abyss = True
while True:
    x, y = SAND_SOURCE
    at_rest = False

    while not at_rest:
        if (x, y+1) not in cave and y+1 != max_y+2:
            y += 1
        elif (x-1, y+1) not in cave and y+1 != max_y+2:
            x -= 1
            y += 1
        elif (x+1, y+1) not in cave and y+1 != max_y+2:
            x += 1
            y += 1
        # sand at rest
        else:
            cave[(x, y)] = 'o'
            at_rest = True
            resting_sand += 1
            if (x, y) == SAND_SOURCE:
                break

        # sand entering "endless void"
        if abyss and x < min_x or x > max_x or y >= max_y:
            abyss = False
            # print('Part 1:', resting_sand)

    else:
        continue
    break

# display_cave()
# submit(resting_sand)
