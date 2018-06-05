from __future__ import division

def partition(A, k=1):
    if k == 1: return [A]
    left, right = partition_ratio(A, left_to_right=k-1)
    return [*partition(left, k=k-1), right]

def partition_ratio(A, left_to_right=1):
    left, right = 0, len(A)-1
    sum_left, sum_right = A[left], A[right]

    while left != right:
        if sum_left/sum_right <= left_to_right:
            left += 1
            sum_left += A[left]
        else:
            right -= 1
            sum_right += A[right]

    return A[:left] , A[right:]


def test():
    print(partition(k=3, A=[1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(partition(k=2, A=[10, 10, 10, 10]))
    print(partition(k=2, A=[10, 20, 30, 40]))
    print(partition(k=5, A=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))


if __name__ == '__main__':
    test()
