from aocd import data, submit


c = data.split('\n\n')

most = 0
elves = []
for elf in c:
    cur = 0
    for x in elf.split():
        cur += int(x)

    # most = max(most, cur)
    elves.append(cur)

# submit(most)
submit(sum(sorted(elves)[-3:]))
