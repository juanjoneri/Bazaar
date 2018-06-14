"""
given an arithmetic equation consisting of positive integers, +, -, *, and / (no parens)
compute the result
"""

import re


APPLY = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    }

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

    def apply(self, a, b):
        return self.APPLY[self.name](a, b)


def compute(equation):
    first, *values = [int(name) for name in re.findall(r'\d+', equation)]
    ops = [Operation(name) for name in re.findall(r'[+\-*/]', equation)]

    values_stack = [first]
    ops_stack = []

    for value, op in zip(values, ops):
        if not any(ops_stack):

            ops_stack.append(op)
            values_stack.append(value)

        elif op <= ops_stack[-1]:
            b, a = values_stack.pop(), values_stack.pop()
            values_stack.append(ops_stack.pop().apply(a, b))

            ops_stack.append(op)
            values_stack.append(value)

        else:
            a = values_stack.pop()
            values_stack.append(op.apply(a, value))


    return ops_stack.pop().apply(*values_stack)






def main():
    print(compute('2*3+5/6*3+15'))
    print(compute('2-6-7*8/2+5'))

if __name__ == '__main__':
    main()
