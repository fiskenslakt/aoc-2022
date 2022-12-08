from collections import defaultdict
from functools import reduce
from operator import mul

from aocd import lines, submit

# lines = '''30373
# 25512
# 65332
# 33549
# 35390'''.splitlines()

# lines = '''1111
# 1214
# 1110'''.splitlines()

# with open('test.in') as f:
#     lines = f.read().splitlines()

visible = 0
scenic = defaultdict(list)
# import pudb;pu.db

for y, line in enumerate(lines):
    for x, tree in enumerate(line):
        if x == 0 or x == len(line) - 1:
            visible += 1
            continue
        elif y == 0 or y == len(lines) - 1:
            visible += 1
            continue
        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x
            ny = y
            while 0 < nx < len(line) - 1 and 0 < ny < len(lines) - 1:
                nx += i
                ny += j
                if int(lines[ny][nx]) >= int(tree):
                    break
            else:
                visible += 1
                break

for y, line in enumerate(lines):
    for x, tree in enumerate(line):
        # if x == 2 and y == 3:
        #     import pudb;pu.db
        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            trees = 0
            nx = x
            ny = y
            while 0 < nx < len(line) - 1 and 0 < ny < len(lines) - 1:
                nx += i
                ny += j
                if int(lines[ny][nx]) >= int(tree):
                    trees += 1
                    break
                else:
                    trees += 1
            scenic[(x, y)].append(trees)

print('Part 1:', visible)
best = max(scenic.items(), key=lambda t: reduce(mul, t[1]))
print(reduce(mul, best[1]), best)
submit(reduce(mul, best[1]))
