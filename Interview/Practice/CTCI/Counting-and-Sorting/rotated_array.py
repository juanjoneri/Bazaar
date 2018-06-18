"""
Given a sorted array of n integers that has been rotated an unknown number of times,
write code to find an element in the array. You may assume that the array was sorted in increasing order
"""




def find(array, element):
    if not any(array):
        return -1

    center = len(array) // 2
    if element == array[center]:
        return center

    if array[0] < array[center]:
        # left is sorted
        if array[0] <= element < array[center]:
            # binary search left
            return find(array[:center], element)
        else:
            # recurse on right, it migh be there
            return center + find(array[center:], element)

    elif array[-1] > array[center]:
        # right is sorted
        if array[center] < element <= array[-1]:
            # binary search right
            return center + find(array[center:], element)
        else:
            # recurse left, it might be there
            return find(array[:center], element)



def main():
    assert find([6, 7, 8, 1, 2, 3, 4, 5], 4) == 6
    assert find([6, 7, 8, 1, 2, 3, 4, 5], 5) == 7
    assert find([6, 7, 8, 1, 2, 3, 4, 5], 6) == 0
    assert find([6, 7, 8, 1, 2, 3, 4, 5], 7) == 1

    assert find([1, 2, 3, 4], 3) == 2
    assert find([1, 0], 0) == 1
    assert find([10, 11, 12, 13, 14, 0, 1, 2], 0) == 5

if __name__ == '__main__':
    main()
