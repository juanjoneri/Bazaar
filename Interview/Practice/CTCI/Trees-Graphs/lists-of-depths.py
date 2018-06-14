"""
Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth.
"""
from collections import defaultdict

class Node():
    def __init__(self, id):
        self.id = id
        self._left = None
        self._right = None
        self.level = 0

    def __str__(self):
        return str(self.id)

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, other):
        self._left = other
        other.level = self.level + 1

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, other):
        self._right = other
        other.level = self.level + 1

def connect_levels(root, levels=None):

    if levels is None:
        levels = defaultdict(list)

    if root is not None:
        levels[root.level].append(root)
        connect_levels(root.left, levels)
        connect_levels(root.right, levels)

    return levels


def main():
    nodes = [Node(i) for i in range(7)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]

    levels = connect_levels(nodes[0])
    for k, v in levels.items():
        print(k, list(map(str, v)))

if __name__ == '__main__':
    main()
