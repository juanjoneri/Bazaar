"""
Implement a MyQueue class which implements a queue using two stacks.
"""


class Stack():
    """stack"""
    def __init__(self):
        self._elements = []

    def push(self, element):
        return self._elements.append(element)

    def pop(self):
        return self._elements.pop()

    @property
    def empty(self):
        return not any(self._elements)

class MyQueue():
    """queue"""
    def __init__(self):
        self._left_stack = Stack() # main stack
        self._right_stack = Stack() # helper stack

    def enqueue(self, element):
        return self._left_stack.push(element)

    def dequeue(self):
        self._swap_right()
        element = self._right_stack.pop()
        self._swap_left()
        return element

    def _swap_right(self):
        while not self._left_stack.empty:
            self._right_stack.push(self._left_stack.pop())

    def _swap_left(self):
        while not self._right_stack.empty:
            self._left_stack.push(self._right_stack.pop())

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
