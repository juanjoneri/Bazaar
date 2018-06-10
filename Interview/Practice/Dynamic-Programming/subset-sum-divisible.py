"""
Given a set of non-negative distinct integers, and a value m, determine if there is a subset of the given set with sum divisible by m.
Input Constraints

Input : arr[] = {3, 1, 7, 5};
        m = 6;
Output : YES

Input : arr[] = {1, 6};
        m = 5;
Output : NO
"""

def subset_sum_divisible_by(numbers, divisor):
    if divisor < len(numbers):
        return True

    if not any(numbers):
        return False
