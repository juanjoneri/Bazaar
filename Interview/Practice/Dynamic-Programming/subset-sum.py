"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
"""

def subset_sum(numbers, total):
    if total == 0:
        return True

    if not any(numbers):
        return False

    subset = numbers.copy()
    last = subset.pop()
    return subset_sum(subset, total - last) or subset_sum(subset, total)

if __name__ == '__main__':
    assert subset_sum({3, 34, 4, 12, 5, 2}, 9)
    assert subset_sum({}, 0)
    assert subset_sum({3, 34, 4, 12, 5, 2}, 0)
    assert subset_sum({3, 34, 4, 12, 5, 2}, 2)

    assert not subset_sum({3, 34, 4, 12, 5, 2}, 1)
    assert not subset_sum({}, 2)
