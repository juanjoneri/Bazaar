"""
given an arithmetic equation consisting of positive integers, +, -, *, and / (no parens)
compute the result
"""

import re
from collections import deque

class Operation():
    PRIORITY = '*/'
    APPLY = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        }

    def __init__(self, name):
        self.name = name
        self.priority = 1 if name in self.PRIORITY else 0

    def __str__(self):
        return self.name

    def __le__(self, other):
        return self.priority <= other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __call__(self, a, b):
        return self.APPLY[self.name](a, b)


def compute(equation):
    first_value, second_value, *values = [int(name) for name in re.findall(r'\d+', equation)]
    first_op, *ops = [Operation(name) for name in re.findall(r'[+\-*/]', equation)]

    values_stack = deque([first_value, second_value])
    ops_stack = deque([first_op])

    for value, op in zip(values, ops):
        if op <= ops_stack[-1]:
            # first apply last operation if it has higher precedence
            b, a = values_stack.pop(), values_stack.pop()
            values_stack.append(ops_stack.pop()(a, b))

            ops_stack.append(op)
            values_stack.append(value)

        else:
            # first apply this operation
            a = values_stack.pop()
            values_stack.append(op(a, value))

    return ops_stack.pop()(*values_stack)






def main():
    assert compute('2*3+5/6*3+15') == 23.5
    assert compute('2-6-7*8/2+5') == -27
    assert compute('1+1') == 2
    assert compute('2*3') == 6
    assert compute('2*2/2*2/2*2/2*2/2') == 2

if __name__ == '__main__':
    main()
