import re
from aocd import lines

MAX_SIZE = 100_000
TOTAL_DISKSPACE = 70_000_000
UPDATE_SIZE = 30_000_000
CMD_PATTERN = re.compile(r'\$ (cd|ls) ?(\.\.|\w+|/)?')
FILE_PATTERN = re.compile(r'(\d+) (.+)')


class Node:
    def __init__(self, name, parent=None, size=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def __repr__(self):
        return f'Node({self.name}, {self.size})'


def find_files(node):
    dir_size = 0
    child_dir_sizes = []
    for child in node.children:
        if child.size is not None:
            dir_size += child.size
        else:
            child_dir_size, grandchildren_sizes = find_files(child)
            dir_size += child_dir_size
            child_dir_sizes.append(child_dir_size)
            child_dir_sizes.extend(grandchildren_sizes)

    return dir_size, child_dir_sizes


root = Node('/')
cur_node = None

for line in lines:
    if line.startswith('$'):
        cmd, arg = CMD_PATTERN.search(line).groups()
        if cmd == 'cd':
            if arg == '/':
                cur_node = root
            elif arg == '..':
                cur_node = cur_node.parent
            else:
                new_node = Node(arg, cur_node)
                cur_node.children.append(new_node)
                cur_node = new_node

    elif file_data := FILE_PATTERN.search(line):
        size, name = file_data.groups()
        new_node = Node(name, cur_node, int(size))
        cur_node.children.append(new_node)

total_used_space, file_sizes = find_files(root)
print('Part 1:', sum(size for size in file_sizes if size <= MAX_SIZE))

unused_space = TOTAL_DISKSPACE - total_used_space
space_needed = UPDATE_SIZE - unused_space
for size in sorted(file_sizes):
    if size >= space_needed:
        print('Part 2:', size)
        break
