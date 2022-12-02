from aocd import lines

rps = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
manual = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
          'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
shape_points = {'rock': 1, 'paper': 2, 'scissors': 3}

incorrect_score = 0
correct_score = 0
for line in lines:
    elf, me = line.split()
    elf_choice = manual[elf]
    me_choice = manual[me]

    if elf_choice == me_choice:
        incorrect_score += shape_points[me_choice] + 3
    elif rps[elf_choice] == me_choice:
        incorrect_score += shape_points[me_choice]
    else:
        incorrect_score += shape_points[me_choice] + 6

    if me == 'X':    # lose
        correct_score += shape_points[rps[elf_choice]]
    elif me == 'Y':  # draw
        correct_score += shape_points[elf_choice] + 3
    elif me == 'Z':  # win
        me_choice = rps[rps[elf_choice]]
        correct_score += shape_points[me_choice] + 6

print('Part 1:', incorrect_score)
print('Part 2:', correct_score)
