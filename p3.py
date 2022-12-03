from aocd import lines, submit
from more_itertools import chunked

# lines = '''vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw'''.splitlines()

t = 0
for line in lines:
    r1 = line[:len(line)//2]
    r2 = line[len(line)//2:]

    same = (set(r1) & set(r2)).pop()
    # print(same, ord(same), ord(same) - 38)
    if same.islower():
        t += ord(same) - 96
    else:
        t += ord(same) - 38

# submit(t)
t2 = 0
for g1, g2, g3 in chunked(lines, 3):
    badge = (set(g1) & set(g2) & set(g3)).pop()
    if badge.islower():
        t2 += ord(badge) - 96
    else:
        t2 += ord(badge) - 38

submit(t2)
