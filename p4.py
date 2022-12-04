from aocd import lines

full_overlaps = 0
all_overlaps = 0
for line in lines:
    p1, p2 = line.split(',')

    p1 = tuple(map(int, p1.split('-')))
    p2 = tuple(map(int, p2.split('-')))

    p1, p2 = sorted((p1, p2), key=lambda p: (p[0],-p[1]))
    if p1[1] >= p2[1]:
        full_overlaps += 1
        all_overlaps += 1
    elif p1[0] <= p2[0] <= p1[1]:
        all_overlaps += 1

print('Part 1:', full_overlaps)
print('Part 2:', all_overlaps)
