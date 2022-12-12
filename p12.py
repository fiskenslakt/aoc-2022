from collections import deque

from aocd import lines, submit

# lines = '''Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi'''.splitlines()

graph = {}
queue = deque()
for y, row in enumerate(lines):
    for x, col in enumerate(row):
        graph[(x,y)] = col
        if col == 'S':
            start = (x, y)
        elif col == 'a':
            queue.append(((x, y), 0))

# import pudb;pu.db
visited = {start}
# queue = deque([(start, 0, [start])])
while queue:
    # (x, y), steps, path = queue.popleft()
    (x, y), steps = queue.popleft()

    if lines[y][x] == 'E':
        print(steps, path)
        break

    for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
        nx = x+i
        ny = y+j

        if (nx < 0 or nx >= len(lines[0])
                or ny < 0 or ny >= len(lines)):
            continue

        cur_cell = lines[y][x]
        new_cell = lines[ny][nx]
        if (cur_cell == new_cell or ord(cur_cell) + 1 == ord(new_cell) or new_cell in 'ab' or (ord(cur_cell) > ord(new_cell) and new_cell.islower())) and (nx,ny) not in visited:
            # queue.append(((nx,ny), steps+1, path+[(nx,ny)]))
            queue.append(((nx,ny), steps+1))
            visited.add((nx,ny))
        elif cur_cell == 'z' and new_cell == 'E':
            submit(steps+1)
            break
else:
    print('not found')
