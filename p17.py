from itertools import cycle

from aocd import data as jet_pattern, submit

# jet_pattern = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''

'''####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##'''

ROCKS = (
    ((0,0), (1,0), (2,0), (3,0)),
    ((1,0), (0,1), (1,1), (2,1), (1,2)),
    ((0,0), (1,0), (2,0), (2,1), (2,2)),
    ((0,0), (0,1), (0,2), (0,3)),
    ((0,0), (1,0), (0,1), (1,1)),
)

highest_point = 0
resting_rocks = 0
chamber = {(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0)}
jet_idx = 0

# import pudb;pu.db

for rock in cycle(ROCKS):
    if resting_rocks == 2022:
        break
    if resting_rocks == 1_000_000_000_000:
        break

    x, y = 2, highest_point + 4
    while True:
        if jet_pattern[jet_idx] == '>':
            nx = x + 1
        elif jet_pattern[jet_idx] == '<':
            nx = x - 1

        jet_idx = (jet_idx + 1) % len(jet_pattern)

        for rx, ry in rock:
            if rx + nx < 0 or rx + nx > 6 or (rx+nx, ry+y) in chamber:
                break
        else:
            x = nx

        ny = y - 1

        for rx, ry in rock:
            if (rx+x, ry+ny) in chamber:
                highest_point = max(highest_point, max(rock, key=lambda r: r[1])[1] + y)
                resting_rocks += 1
                for rx, ry in rock:
                    chamber.add((rx+x,ry+y))
                break
        else:
            y = ny
            continue
        break

submit(highest_point)
