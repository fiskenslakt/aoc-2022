from collections import defaultdict

from aocd import lines

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

            # Either laterally adjacent or overlapping
            if (tail.real == head.real and abs(tail.imag - head.imag) <= 1
                    or tail.imag == head.imag and abs(tail.real - head.real) <= 1):
                continue

            # Diagonally adjacent
            if (tail + 1+1j == head
                    or tail - 1+1j == head
                    or tail + 1-1j == head
                    or tail - 1-1j == head):
                continue

            # More than 2 steps away
            if head - tail in normal_moves:
                rope[knot_idx] += normal_moves[head - tail]
            elif head - tail in knight_moves:
                rope[knot_idx] += knight_moves[head - tail]
            elif head - tail in diagonal_moves:
                rope[knot_idx] += diagonal_moves[head - tail]

            short_rope_grid[rope[1]] += 1
            long_rope_grid[rope[9]] += 1

print('Part 1:', sum(v > 0 for v in short_rope_grid.values()))
print('Part 2:', sum(v > 0 for v in long_rope_grid.values()))
