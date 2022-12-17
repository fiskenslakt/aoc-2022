from itertools import cycle

from aocd import data as jet_pattern

ROCKS = (
    ((0,0), (1,0), (2,0), (3,0)),
    ((1,0), (0,1), (1,1), (2,1), (1,2)),
    ((0,0), (1,0), (2,0), (2,1), (2,2)),
    ((0,0), (0,1), (0,2), (0,3)),
    ((0,0), (1,0), (0,1), (1,1)),
)

highest_point = 0
resting_rocks = 0
# Initialize chamber with a floor.
chamber = {(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0)}
jet_idx = 0
prev_states = {}
part1, part2 = False, False


for rock in cycle(ROCKS):
    if resting_rocks == 2022:
        part1 = True
        print('Part 1:', highest_point)

    if part1 and part2:
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

                fingerprint = ''
                for j in range(highest_point, highest_point-20, -1):
                    for i in range(7):
                        if (i,j) in chamber:
                            fingerprint += '#'
                        else:
                            fingerprint += ' '

                state = (rock, jet_idx, fingerprint)
                if state in prev_states and not part2:
                    part2 = True
                    cycle_length = resting_rocks - prev_states[state][1]
                    height_delta = highest_point - prev_states[state][0]
                else:
                    prev_states[state] = (highest_point, resting_rocks)
                break
        else:
            y = ny
            continue
        break

rock_delta = int(1e12) % cycle_length
height_offset = list(prev_states.values())[rock_delta-1][0]
resting_rocks_extreme_edition = int(1e12 // cycle_length * height_delta) + height_offset
print('Part 2:', resting_rocks_extreme_edition)
