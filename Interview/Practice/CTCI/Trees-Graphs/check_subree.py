"""
T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return f'{self.left}({self.value}){self.right}'

    def has_subtree(self, other):
        for possible_root in self.descendant_with_value(other.value):
            if Node.same_tree(possible_root, other):
                return True

        return False

    @staticmethod
    def same_tree(T1, T2):
        if T1 is None or T2 is None:
            return T1 is T2

        same_root = T1.value == T2.value
        same_left = Node.same_tree(T1.left, T2.left)
        same_right = Node.same_tree(T1.right, T2.right)

        return same_root and same_left and same_right

    def descendant_with_value(self, value):
        if self.value == value:
            yield self

        if self.left is not None:
            yield from self.left.descendant_with_value(value)

        if self.right is not None:
            yield from self.right.descendant_with_value(value)

def main():
    T1 = Node(10)
    T1.left, T1.right = Node(5), Node(-3)
    T1.left.left, T1.left.right = Node(3), Node(2)
    T1.right.right = Node(11)

    T1.left.left.left, T1.left.left.right = Node(3), Node(-2)
    T1.left.right.right = Node(1)

    assert T1.has_subtree(T1)
    assert T1.has_subtree(Node(11))
    assert T1.has_subtree(Node(1))
    assert not T1.has_subtree(Node(10))
    assert not T1.has_subtree(Node(-1))

    T2 = Node(3)
    T2.left, T2.right = Node(3), Node(-2)
    assert T1.has_subtree(T2)

    T2 = Node(5)
    T2.left, T2.right = Node(3), Node(2)

    assert not T1.has_subtree(T2)

if __name__ == '__main__':
    main()
