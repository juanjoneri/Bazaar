"""
You are given a binary tree in which each node contains an integer value.
Design an algorithm to count the number os paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards.
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return f'{self.left}({self.value}){self.right}'

    def paths_that_sum(self, target):
        total = 1 if target == self.value else 0
        if self.left is not None:
            total += self.left.paths_that_sum(target)
            total += self.left.paths_that_sum_ending(target-self.value)

        if self.right is not None:
            total += self.right.paths_that_sum(target)
            total += self.right.paths_that_sum_ending(target-self.value)

        return total

    def paths_that_sum_ending(self, target):
        if target == self.value:
            return 1

        total = 0
        if self.left is not None:
            total += self.left.paths_that_sum_ending(target-self.value)

        if self.right is not None:
            total += self.right.paths_that_sum_ending(target-self.value)

        return total



def main():
    root = Node(10)
    root.left, root.right = Node(5), Node(-3)
    root.left.left, root.left.right = Node(3), Node(2)
    root.right.right = Node(11)

    root.left.left.left, root.left.left.right = Node(3), Node(-2)
    root.left.right.right = Node(1)

    assert root.paths_that_sum(8) == 3
    assert root.paths_that_sum(10) == 1
    assert root.paths_that_sum(7) == 2
    assert root.paths_that_sum(3) == 3


if __name__ == '__main__':
    main()
