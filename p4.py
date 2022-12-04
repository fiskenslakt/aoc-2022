from aocd import lines, submit

# lines = '''2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8'''.splitlines()

c = 0
c2 = 0
for line in lines:
    p1, p2 = line.split(',')

    p1a, p1b = p1.split('-')
    p1 = tuple(map(int, p1.split('-')))
    p2a, p2b = p2.split('-')
    p2 = tuple(map(int, p2.split('-')))

    x = sorted((p1, p2), key=lambda p: (p[0],-p[1]))
    if x[0][1] >= x[1][1]:
        c += 1
        c2 += 1
    elif x[0][0] <= x[1][0] <= x[0][1]:
        c2 += 1

# submit(c)
submit(c2)
