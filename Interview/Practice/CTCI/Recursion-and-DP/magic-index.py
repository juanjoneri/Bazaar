"""
A magic index in an array A[0, ,n-1] is defined to be an index such that A[i] == i.
Given a sorted array of dictinct integers, write a method to find a magic index, if one exists, in array A
"""

def magic_index(A, start, end):
    if start > end:
        return None

    center = (end + start) // 2

    if A[center] == center:
        return center

    if A[center] < center:
        magic_right = magic_index(A, center+1, end)
        if magic_right != None:
            return magic_right
    else:
        magic_left = magic_index(A, start, center-1)
        if magic_left != None:
            return magic_left

def main():
    assert magic_index([-1, 1, 3, 4, 5], 0, 4) == 1
    assert magic_index([-1, 0, 2, 4, 5], 0, 4) == 2
    assert magic_index([-1, 0, 1, 2, 4], 0, 4) == 4


if __name__ == '__main__':
    main()
