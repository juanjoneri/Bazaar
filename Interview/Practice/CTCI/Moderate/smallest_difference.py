"""
Given two arrays of integers, copute the pair of values with the smallest absolute difference
"""

import sys

def closest_pair(left, right):
    left, right = iter(sorted(left)), iter(sorted(right))
    current_left, current_right = next(left), next(right)
    smallest_dif = sys.maxsize

    while any(left) or any(right):
        current_dif = current_left - current_right
        smallest_dif = min(smallest_dif, abs(current_dif))

        try:
            if current_dif > 0:
                print('too big')
                current_right = next(right)
            elif current_dif < 0:
                print('too small')
                current_left = next(left)
            else:
                return current_dif

        except StopIteration:
            break

    return smallest_dif



def main():
    left = [1, 3, 15, 11 ,2]
    right = [23, 127, 235, 19, 8]

    print(closest_pair(left, right))

if __name__ == '__main__':
    main()
