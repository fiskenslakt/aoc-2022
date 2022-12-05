import re
from aocd import data, submit
from collections import defaultdict

stacks = defaultdict(list)

stack_data, move_data = data.split('\n\n')

cur_stack = 0
last_char = ''
for chars in zip(*stack_data.splitlines()):
    # if not last_char.isalpha() and char.isalpha():
    #     cur_stack += 1
    # last_char = char

    # if char.isalpha():
    #     stacks[cur_stack].append(char)
    if chars[-1].isdigit():
        for char in chars[-2::-1]:
            if char.isalpha():
                stacks[chars[-1]].append(char)

# for move in move_data.splitlines():
#     n, s1, s2 = re.findall('\d+', move)

#     for _ in range(int(n)):
#         stacks[s2].append(stacks[s1].pop())

for move in move_data.splitlines():
    n, s1, s2 = re.findall('\d+', move)

    temp_stack = []
    for _ in range(int(n)):
        temp_stack.append(stacks[s1].pop())

    for _ in range(int(n)):
        stacks[s2].append(temp_stack.pop())

ans = ''
for i in range(1,10):
    ans += stacks[str(i)][-1]
    # print(stacks[str(i)][-1], end='')

submit(ans)
