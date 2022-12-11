import re

from aocd import lines

INSTRUCTION_PATTERN = re.compile(r'(noop|addx) ?(-?\d+)?')
NOTABLE_CYCLES = (20, 60, 100, 140, 180, 220)

cycle = 0
x_register = 1
signal_strengths = []
screen = ''


def get_pixel(cycle, register):
    pixel = ''
    if (cycle - 1) % 40 == 0:
        pixel += '\n'

    if (register - 1) <= (cycle-1) % 40 <= (register + 1):
        pixel += '█'
    else:
        pixel += ' '

    return pixel


def capture_signal_strength(cycle, register):
    if cycle in NOTABLE_CYCLES:
        signal_strengths.append(cycle * register)


for instruction in lines:
    op, value = INSTRUCTION_PATTERN.search(instruction).groups()
    if op == 'noop':
        cycle += 1
        screen += get_pixel(cycle, x_register)
        capture_signal_strength(cycle, x_register)
    elif op == 'addx':
        for _ in range(2):
            cycle += 1
            screen += get_pixel(cycle, x_register)
            capture_signal_strength(cycle, x_register)
        x_register += int(value)

print('Part 1:', sum(signal_strengths))
print('Part 2:\n', screen)
