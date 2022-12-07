import re
from aocd import lines, submit

MAX_SIZE = 100_000
TOTAL_DISKSPACE = 70_000_000
UPDATE_SIZE = 30_000_000


class Node:
    def __init__(self, name, parent=None, size=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def __repr__(self):
        return f'Node({self.name}, {self.size})'

class Tree:
    small_files = []
    all_files = []

    def __init__(self):
        self.root = Node('/')


cmd_pattern = re.compile(r'\$ (cd|ls) ?(\.\.|\w+|/)?')
file_pattern = re.compile(r'(\d+) (.+)')
fs = Tree()
cur_node = None

for line in lines:
    if line.startswith('$'):
        cmd = cmd_pattern.search(line)
        if cmd[1] == 'cd':
            if cmd[2] == '/':
                cur_node = fs.root
            elif cmd[2] == '..':
                cur_node = cur_node.parent
            else:
                new_node = Node(cmd[2], cur_node)
                cur_node.children.append(new_node)
                cur_node = new_node

    if line.startswith('dir'):
        pass

    if m := file_pattern.search(line):
        size, name = m.groups()
        new_node = Node(name, cur_node, int(size))
        cur_node.children.append(new_node)

def find_files(node):
    total_size = 0
    for child in node.children:
        if child.size is not None:
            total_size += child.size
        else:
            total_size += find_files(child)

    if total_size <= MAX_SIZE:
        fs.small_files.append(total_size)
    fs.all_files.append(total_size)

    return total_size

total_used_space = find_files(fs.root)
# submit(sum(fs.small_files))

unused_space = TOTAL_DISKSPACE - total_used_space
space_needed = UPDATE_SIZE - unused_space
for size in sorted(fs.all_files):
    if size >= space_needed:
        submit(size)
        break
