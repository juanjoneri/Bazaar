"""
Implement a MyQueue class which implements a queue using two stacks.
"""
from collections import deque

class MyQueue():
    """queue"""
    def __init__(self):
        self._left_stack = deque() # main stack
        self._right_stack = deque() # helper stack

    def enqueue(self, element):
        return self._left_stack.append(element)

    def dequeue(self):
        self._swap_right()
        element = self._right_stack.pop()
        self._swap_left()
        return element

    def _swap_right(self):
        while any(self._left_stack):
            self._right_stack.append(self._left_stack.pop())

    def _swap_left(self):
        while any(self._right_stack):
            self._left_stack.append(self._right_stack.pop())

def main():
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4

if __name__ == '__main__':
    main()
