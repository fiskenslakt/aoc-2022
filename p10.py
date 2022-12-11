import re

from aocd import lines, submit

INSTRUCTION_PATTERN = re.compile(r'(noop|addx) ?(-?\d+)?')
NOTABLE_CYCLES = (20, 60, 100, 140, 180, 220)

# with open('example10.in') as f:
#     lines = f.read().splitlines()

cycle = 0
pointer = 0
x_register = 1
signal_strengths = []

cycles_to_complete = 0
last_pointer = None
# import pudb;pu.db
# while True:
#     if cycle == 0:
#         instruction = lines[pointer]
#         op, value = INSTRUCTION_PATTERN.search(instruction).groups()
#         # pointer += 1

#     if cycle in NOTABLE_CYCLES:
#         signal_strengths.append(cycle * x_register)

#     if cycles_to_complete == 0 and last_pointer != pointer:
#         if op == 'noop':
#             cycles_to_complete = 1
#         elif op == 'addx':
#             cycles_to_complete = 2
#         else:
#             raise Exception('wtf?')
#         last_pointer = pointer

#     if cycles_to_complete == 0:
#         if op == 'addx':
#             x_register += int(value)
#         if op == 'noop':
#             cycle += 1
#         pointer += 1
#         if pointer == len(lines):
#             break
#         instruction = lines[pointer]
#         op, value = INSTRUCTION_PATTERN.search(instruction).groups()
#         continue

#     cycle += 1
#     cycles_to_complete -= 1
def capture_signal_strength(cycle, register):
    if cycle in NOTABLE_CYCLES:
        signal_strengths.append(cycle * register)

for instruction in lines:
    op, value = INSTRUCTION_PATTERN.search(instruction).groups()
    if op == 'noop':
        cycle += 1
        capture_signal_strength(cycle, x_register)
    elif op == 'addx':
        cycle += 1
        capture_signal_strength(cycle, x_register)
        cycle += 1
        capture_signal_strength(cycle, x_register)
        x_register += int(value)

# print(signal_strengths, sum(signal_strengths))
submit(sum(signal_strengths))
