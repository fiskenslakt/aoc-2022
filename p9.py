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
diagonal_moves = {
     2+2j:  1+1j,
    -2+2j: -1+1j,
    -2-2j: -1-1j,
     2-2j:  1-1j,
}

short_rope_grid = defaultdict(int)
long_rope_grid = defaultdict(int)
rope = [0j]*10

short_rope_grid[rope[1]] += 1
long_rope_grid[rope[9]] += 1

# import pudb;pu.db

for line in lines:
    d, n = line.split()
    for _ in range(int(n)):
        if d == 'R':
            rope[0] += 1
        elif d == 'L':
            rope[0] -= 1
        elif d == 'U':
            rope[0] += 1j
        elif d == 'D':
            rope[0] -= 1j

        for knot_idx, tail in enumerate(rope[1:], 1):
            head = rope[knot_idx-1]

            if (tail.real == head.real and abs(tail.imag - head.imag) <= 1
                    or tail.imag == head.imag and abs(tail.real - head.real) <= 1):
                continue

            if (tail + 1+1j == head
                    or tail - 1+1j == head
                    or tail + 1-1j == head
                    or tail - 1-1j == head):
                continue

            if head - tail in normal_moves:
                rope[knot_idx] += normal_moves[head - tail]
            elif head - tail in knight_moves:
                rope[knot_idx] += knight_moves[head - tail]
            elif head - tail in diagonal_moves:
                rope[knot_idx] += diagonal_moves[head - tail]

            short_rope_grid[rope[1]] += 1
            long_rope_grid[rope[9]] += 1

print('Part 1:', (sum(v > 0 for v in short_rope_grid.values())))
# print(rope)
submit(sum(v > 0 for v in long_rope_grid.values()))

#5 .H.H..
#4 H...H.
#3 ..T...
#2 H...H.
#1 .H.H..
#  123456

#5 ...TH.
#4 ......
#3 .3....
#2 ......
#1 ......
#  123456
