from collections import deque

from aocd import lines

CUBE_SIDES = ((0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0))


def bfs(x, y, z):
    seen = set()
    queue = deque([(x, y, z)])

    while queue:
        x, y, z = queue.popleft()

        if x > max_x or y > max_y or z > max_z:
            return True
        if x < min_x or y < min_y or z < min_z:
            return True

        for nx, ny, nz in CUBE_SIDES:
            if ((x+nx, y+ny, z+nz) not in grid
                    and (x+nx, y+ny, z+nz) not in seen):
                queue.append((x+nx, y+ny, z+nz))
                seen.add((x+nx, y+ny, z+nz))

    return False


grid = set()
min_x = float('inf')
min_y = float('inf')
min_z = float('inf')
max_x = 0
max_y = 0
max_z = 0

for line in lines:
    x, y, z = map(int, line.split(','))
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    min_z = min(min_z, z)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    max_z = max(max_z, z)

    grid.add((x,y,z))

exposed_sides = 0
for x, y, z in grid:
    sides = 6

    for nx, ny, nz in CUBE_SIDES:
        if (x+nx, y+ny, z+nz) in grid:
            sides -= 1

    exposed_sides += sides

print('Part 1:', exposed_sides)

exposed_sides = 0
for x, y, z in grid:
    sides = 0

    for nx, ny, nz in CUBE_SIDES:
        if (x+nx, y+ny, z+nz) not in grid and bfs(x+nx, y+ny, z+nz):
            sides += 1

    exposed_sides += sides

print('Part 2:', exposed_sides)
