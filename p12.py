from collections import deque

from aocd import lines


def bfs(queue):
    visited = set()
    while queue:
        (x, y), steps = queue.popleft()

        for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
            nx = x+i
            ny = y+j

            if (nx < 0 or nx >= len(lines[0])
                    or ny < 0 or ny >= len(lines)):
                continue

            cur_cell = lines[y][x]
            new_cell = lines[ny][nx]
            if (nx, ny) in visited:
                continue

            if new_cell == 'E':
                if cur_cell == 'z':
                    return steps + 1
                continue

            if (cur_cell == new_cell
                    or ord(cur_cell) + 1 == ord(new_cell)
                    or new_cell == 'a'
                    or cur_cell > new_cell):
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))


a_queue = deque()
s_queue = deque()
for y, row in enumerate(lines):
    for x, col in enumerate(row):
        if col == 'S':
            s_queue.append(((x, y), 0))
        elif col == 'a':
            a_queue.append(((x, y), 0))

print('Part 1:', bfs(s_queue))
print('Part 2:', bfs(a_queue))
