"""
Imagine a robot sitting on the upper left corner of a grid with r rows and c columnsself.
The robot can onl ymove in two directions, right and down, but certain cellas are off limits `False`, such that the robot cannot step on them.
Design an algorithm to find the path for the robot from the top left to the bottom right
"""

import sys

def get_neighbors(grid, position):
    """yield up and/or left depending on which are available"""
    row, col = position
    if row != 0 and grid[row-1][col]:
        yield row-1, col
    if col != 0 and grid[row][col-1]:
        yield row, col-1


def robot(grid, current):
    if current == (0, 0):
        return 0

    neighbors = list(get_neighbors(grid, current))

    if not any(neighbors):
        return sys.maxsize

    return 1 + min([robot(grid, neighbor) for neighbor in neighbors])




def main():
    grid = [[True, True, False, False],
            [True, False, False, False],
            [True, True, False, True],
            [False, True, True, True],
            [False, True, False, True],
            [True, True, False, True]]

    current = len(grid)-1, len(grid[-1])-1

    assert robot(grid, current) == 8

if __name__ == '__main__':
    main()
