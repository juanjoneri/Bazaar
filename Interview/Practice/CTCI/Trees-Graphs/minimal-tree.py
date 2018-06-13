"""
Given a sorted (incresing) array with unique integers elements,
write an algorithm to create a binary sarch tree with min height
"""

class Node():
    def __init__(self, id):
        self.id = id
        self.smaller = None
        self.bigger = None

    def __str__(self):
        return f'{self.id} -> ({self.smaller}, {self.bigger})'


def construct_tree(nodes):
    if not any(nodes):
        return None

    center = len(nodes) // 2
    root = nodes[center]

    root.smaller = construct_tree(nodes[:center])
    root.bigger = construct_tree(nodes[center+1:])

    return root



def main():
    nodes = [Node(i) for i in range(0, 21, 2)]
    root = construct_tree(nodes)
    print(root)

if __name__ == '__main__':
    main()
