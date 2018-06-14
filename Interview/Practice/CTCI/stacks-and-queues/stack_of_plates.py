"""
Implement a stack of plates that behaves ecactly like a stack, but using multiple
stacks, each of which cannot exceed a maximun height
"""

class StackOfPlates():
    def __init__(self, max_height):
        self.max_height = max_height
        self._stacks = [[]]

    def __str__(self):
        return str(list(map(str, self._stacks)))

    def push(self, element):
        if self._full:
            self._stacks.append([])

        return self._stacks[-1].append(element)

    def pop(self):
        if not any(self._stacks[-1]):
            self._stacks.pop()
        return self._stacks[-1].pop()

    @property
    def _full(self):
        return len(self._stacks[-1]) == self.max_height


def main():
    stack = StackOfPlates(3)
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    print(stack)

    stack.push(10)
    stack.push(11)
    stack.push(12)
    stack.push(13)
    stack.push(14)
    stack.pop()
    print(stack)

    stack.push(20)
    stack.push(21)
    stack.push(22)
    stack.push(23)
    print(stack)

    stack.pop()
    stack.pop()
    print(stack)

if __name__ == '__main__':
    main()
