import re
from collections import defaultdict

from aocd import data

stacks = {}
stack_data, move_data = data.split('\n\n')

for chars in zip(*stack_data.splitlines()):
    if chars[-1].isdigit():
        stacks[chars[-1]] = defaultdict(list)
        for char in chars[-2::-1]:
            if char.isalpha():
                stacks[chars[-1]]['9000'].append(char)
                stacks[chars[-1]]['9001'].append(char)

for move in move_data.splitlines():
    amount, src, dest = re.findall('\d+', move)

    for _ in range(int(amount)):
        stacks[dest]['9000'].append(stacks[src]['9000'].pop())

    temp_stack = []
    for _ in range(int(amount)):
        temp_stack.append(stacks[src]['9001'].pop())

    for _ in range(int(amount)):
        stacks[dest]['9001'].append(temp_stack.pop())

crates_9000 = ''
crates_9001 = ''
for i in range(1, len(stacks)+1):
    crates_9000 += stacks[str(i)]['9000'][-1]
    crates_9001 += stacks[str(i)]['9001'][-1]

print('Part 1:', crates_9000)
print('Part 1:', crates_9001)
