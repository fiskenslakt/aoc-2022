from functools import cached_property

from aocd import numbers

DECRYPTION_KEY = 811589153


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return f'Node({self.value})'


class LinkedList:
    def __init__(self, coords):
        self.nodes = []
        cur_node = None
        for coord in coords:
            new_node = Node(coord)
            self.nodes.append(new_node)

            if cur_node is not None:
                cur_node.next_node = new_node
                new_node.prev_node = cur_node

            cur_node = new_node

        head = self.nodes[0]
        tail = self.nodes[-1]
        head.prev_node = tail
        tail.next_node = head

    @cached_property
    def zero(self):
        for node in self.nodes:
            if node.value == 0:
                return node

    def get_node(self, node, n):
        if n == 0: return node

        cur_node = node
        for _ in range(abs(n)):
            if n > 0:
                cur_node = cur_node.next_node
            elif n < 0:
                cur_node = cur_node.prev_node

        return cur_node


def move_coord(coord, decryption_key=False):
    if decryption_key:
        moves = coord.value * DECRYPTION_KEY % (len(numbers) - 1)
    else:
        moves = coord.value

    if moves == 0:
        return

    original_prev_node = coord.prev_node
    original_next_node = coord.next_node

    original_prev_node.next_node = original_next_node
    original_next_node.prev_node = original_prev_node

    new_prev_node = coord_file.get_node(original_prev_node, moves)
    new_next_node = new_prev_node.next_node

    new_prev_node.next_node = coord
    coord.prev_node = new_prev_node
    coord.next_node = new_next_node
    new_next_node.prev_node = coord


coord_file = LinkedList(numbers)

for coord in coord_file.nodes:
    move_coord(coord)

x = coord_file.get_node(coord_file.zero, 1_000).value
y = coord_file.get_node(coord_file.zero, 2_000).value
z = coord_file.get_node(coord_file.zero, 3_000).value

print('Part 1:', x + y + z)

coord_file = LinkedList(numbers)

for round in range(1, 11):
    for coord in coord_file.nodes:
        move_coord(coord, True)

x = coord_file.get_node(coord_file.zero, 1_000).value * DECRYPTION_KEY
y = coord_file.get_node(coord_file.zero, 2_000).value * DECRYPTION_KEY
z = coord_file.get_node(coord_file.zero, 3_000).value * DECRYPTION_KEY

print('Part 2:', x + y + z)
