
from collections import defaultdict

class Node():
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.left = self.right = None

    def add_left(self, child):
        child.level = self.level + 1
        self.left = child

    def add_right(self, child):
        child.level = self.level + 1
        self.right = child

    def connect(self, level=0, memo=defaultdict(list)):
        memo[level].append(self)
        if self.left:
            self.left.connect(level+1, memo)
        if self.right:
            self.right.connect(level+1, memo)
        return memo


    def __str__(self):
        return f'{self.name}'

if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')

    a.add_left(b)
    a.add_right(c)
    b.add_left(d)
    b.add_right(e)
    c.add_right(f)

    for k, v in a.connect().items():
        print(k, list(map(str, v)))
