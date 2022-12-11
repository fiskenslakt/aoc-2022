import re
from collections import deque
from operator import add, mul

from aocd import data, submit

# with open('ex11.in') as f:
#     data = f.read()

MONKEY_PATTERN = re.compile(r'Monkey (\d+):\n.+?: (.+)\n.+?= (.+)\n.+?(\d+)\n.+?(\d+)\n.+?(\d+)')
OPERATIONS = {'*': mul, '+': add}

monkeys = {}

for monkey in data.split('\n\n'):
    monkey = MONKEY_PATTERN.search(monkey)
    n_monkey = int(monkey[1])
    items = deque(map(int, monkey[2].split(', ')))
    op = monkey[3].split()
    test = int(monkey[4])
    if_true = int(monkey[5])
    if_false = int(monkey[6])

    monkeys[n_monkey] = {
        'items': items,
        'op': op,
        'test': test,
        'true': if_true,
        'false': if_false,
        'inspections': 0
    }

n_monkeys = n_monkey
# import pudb;pu.db
for round in range(20):
    for n_monkey in range(0, n_monkeys+1):
        monkey = monkeys[n_monkey]

        while monkey['items']:
            item = monkey['items'].popleft()
            monkey['inspections'] += 1
            operand1, operator, operand2 = monkey['op']
            operand1 = item if operand1 == 'old' else int(operand1)
            operand2 = item if operand2 == 'old' else int(operand2)
            item = OPERATIONS[operator](operand1, operand2)
            item //= 3

            if item % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(item)
            else:
                monkeys[monkey['false']]['items'].append(item)

inspections = [monkey['inspections'] for monkey in monkeys.values()]
most_active = sorted(inspections, reverse=True)[:2]
print(inspections)
print(mul(most_active[0], most_active[1]))
