"""
There is a given binary matrix, we need to find if there exists any rectangle or square in the given matrix whose all four corners are equal to 1.

Input :
mat[][] = { 1 0 0 1 0
            0 0 1 0 1
            0 0 0 1 0
            1 0 1 0 1}
Output : Yes
as there exists-
1 0 1
0 1 0
1 0 1
"""

def nonzero_indices(row):
    """return a set with indices of all nonzero elements in the row"""
    return {i for i, v in enumerate(row) if v != 0}

def has_square(matrix):
    """return if the matrix contains a square of rectangle"""
    indices = []
    for row in matrix:
        row_indices = nonzero_indices(row)
        for previous_index in indices:
            if len(row_indices & previous_index) >= 2:
                return True

        indices.append(row_indices)

    return False

if __name__ == '__main__':
    MATRIX = [[1, 0, 0, 1, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 1, 0, 1],
              [0, 0, 0, 1, 0],
              [1, 0, 1, 0, 1]]

    assert has_square(MATRIX)
