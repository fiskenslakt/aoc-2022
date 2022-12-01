from aocd import data


elves = data.split('\n\n')

calorie_sums = []
for elf in elves:
    elf_calories = 0
    for snack in elf.split():
        elf_calories += int(snack)

    calorie_sums.append(elf_calories)

calorie_sums = sorted(calorie_sums, reverse=True)
print('Part 1:', calorie_sums[0])
print('Part 2:', sum(calorie_sums[:3]))
