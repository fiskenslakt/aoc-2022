from aocd import lines, submit

x = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3},
}
y = {'X': 1, 'Y': 2, 'Z': 3}

score = 0
score2 = 0
for line in lines:
    elf, me = line.split()

    score += x[elf][me] + y[me]
    if me == 'X':
        if elf == 'A':
            score2 += 3
        elif elf == 'B':
            score2 += 1
        else:
            score2 += 2
    elif me == 'Y':
        if elf == 'A':
            score2 += 3 + 1
        elif elf == 'B':
            score2 += 3 + 2
        else:
            score2 += 3 + 3
    elif me == 'Z':
        if elf == 'A':
            score2 += 6 + 2
        elif elf == 'B':
            score2 += 6 + 3
        else:
            score2 += 6 + 1


submit(score2)
