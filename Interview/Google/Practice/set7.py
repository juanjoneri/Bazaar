import math

def substring_of_repeated(A, B):
    n, m = len(A), len(B)
    answer = math.ceil(m / n)
    if B in A * answer:
        return answer
    elif B in A * (answer + 1):
        return answer + 1
    return -1


def tests_q1():
    assert substring_of_repeated(A='abcd', B='cdabcdab') == 3
    assert substring_of_repeated(A='abed', B='cdabcdab') == -1
    assert substring_of_repeated(A='cdabcdab', B='abcd') == 1
    assert substring_of_repeated(A='a', B='aa') == 2
    print('All tests passed for question 1')

# ---------------------------------------------------------------
from collections import defaultdict

class Node():
    def __init__(self, label):
        self.label = label
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    @property
    def left_child(self):
        try:
            return self.children[0]
        except:
            return None

    @property
    def right_child(self):
        try:
            return self.children[1]
        except:
            return None

class Tree():
    def __init__(self, A, E):
        self.longest_path = 0
        self.nodes = [None] + [Node(label) for label in A]

        for i in range(len(E)//2):
            parent_index, child_index = E[2*i], E[2*i+1]
            self.nodes[parent_index].add_child(self.nodes[child_index])

        self._longest_path(self.root)

    @property
    def root(self):
        try:
            return self.nodes[1]
        except:
            return None

    def _longest_path(self, root):
        if not root:
            return 0

        left_length = self._longest_path(root.left_child)
        right_length = self._longest_path(root.right_child)

        left_path = right_path = 0
        if root.left_child and root.left_child.label == root.label:
            left_path = left_length + 1
        if root.right_child and root.right_child.label == root.label:
            right_path = right_length + 1

        self.longest_path = max(self.longest_path, left_path + right_path)
        return max(left_path, right_path)




def longest_path(A, E):
    # A[i] is the label of node i+1
    # E[2i] <-> E[2i+1] describe the indexes of an edge
    tree = Tree(A, E)
    return tree.longest_path

def tests_q2():
    print longest_path(A=[1, 1, 1, 2, 2], E=[1, 2, 1, 3, 2, 4, 2, 5])

if __name__ == '__main__':
    tests_q2()
