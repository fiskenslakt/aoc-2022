from collections import defaultdict
from aocd import lines, submit

# lines = '''R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2'''.splitlines()

grid = defaultdict(int)
knight_moves = {
    -2+1j: -1+1j,
    -1+2j: -1+1j,
     1+2j:  1+1j,
     2+1j:  1+1j,
    -2-1j: -1-1j,
    -1-2j: -1-1j,
     1-2j:  1-1j,
     2-1j:  1-1j,
}
normal_moves = {
    -2+0j: -1,
     2+0j:  1,
     0-2j: -1j,
     0+2j:  1j,
}

head = 0j
tail = 0j

grid[tail] += 1

for line in lines:
    d, n = line.split()
    for _ in range(int(n)):
        if d == 'R':
            head += 1
        elif d == 'L':
            head -= 1
        elif d == 'U':
            head += 1j
        elif d == 'D':
            head -= 1j

        if (tail.real == head.real and abs(tail.imag - head.imag) <= 1
                or tail.imag == head.imag and abs(tail.real - head.real) <= 1):
            continue

        if (tail + 1+1j == head
                or tail - 1+1j == head
                or tail + 1-1j == head
                or tail - 1-1j == head):
            continue

        if head - tail in normal_moves:
            tail += normal_moves[head - tail]
        elif head - tail in knight_moves:
            tail += knight_moves[head - tail]

        grid[tail] += 1

submit(sum(v > 0 for v in grid.values()))

#5 .H.H..
#4 H...H.
#3 ..T...
#2 H...H.
#1 .H.H..
#  123456
