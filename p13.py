from ast import literal_eval
from functools import cmp_to_key
from itertools import zip_longest

from aocd import data, submit


def check(left, right):
    if left is None:
        return 1
    elif right is None:
        return -1
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        if not left and not right:
            return 0
        for i, j in zip_longest(left, right):
            result = check(i, j)
            if result == 0:
                continue
            else:
                return result
    elif isinstance(left, list) and isinstance(right, int):
        return check(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return check([left], right)

    return 0


pairs = data.split('\n\n')
indices = []

for i, pair in enumerate(pairs, 1):
    p1, p2 = pair.split()
    p1 = literal_eval(p1)
    p2 = literal_eval(p2)

    result = check(p1, p2)

    if result == 0:
        continue
    elif result == -1:
        pass
    elif result == 1:
        indices.append(i)

print('Part 1:', sum(indices))

divider_packets = [[[2]], [[6]]]
packets = list(map(literal_eval, data.split())) + divider_packets
packets = sorted(packets, key=cmp_to_key(check), reverse=True)

indices = []
for divider_packet in divider_packets:
    indices.append(packets.index(divider_packet) + 1)

print('Part 2:', indices[0] * indices[1])
