from aocd import lines
from more_itertools import chunked

total = 0
for line in lines:
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]

    common_item = (set(compartment1) & set(compartment2)).pop()
    if common_item.islower():
        total += ord(common_item) - 96
    else:
        total += ord(common_item) - 38

print('Part 1:', total)

total = 0
for group1, group2, group3 in chunked(lines, 3):
    badge = (set(group1) & set(group2) & set(group3)).pop()
    if badge.islower():
        total += ord(badge) - 96
    else:
        total += ord(badge) - 38

print('Part 2:', total)
