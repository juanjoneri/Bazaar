"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes
"""

class Node():
    def __init__(self, id):
        self.id = id
        self._children = set()

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def connected_to(self, other, visited=None):
        if visited is None:
            visited = set()

        if self == other:
            return True

        for child in self.children - visited:
            visited.add(child)

            if search(child, other, visited):
                return True

        return False

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, others):
        self._children.update(set(others))




def search(start, end, visited={}):
    if start == end:
        return True

    for child in start.children - visited:
        visited.add(child)

        if search(child, end, visited):
            return True

    return False



def main():
    start = Node(1)
    a, b, c = Node(2), Node(3), Node(4),
    d, e, f = Node(5), Node(6), Node(7)
    end = Node(8)
    start.children = [a, b, c]
    a.children = [d, e]
    b.children = [f]
    e.children = [end]

    assert start.connected_to(end)
    assert b.connected_to(f)
    assert not a.connected_to(f)
    assert not b.connected_to(end)


if __name__ == '__main__':
    main()
