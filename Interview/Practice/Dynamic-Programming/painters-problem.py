"""
We have to paint n boards of length {A1, A2…An}. There are k painters available and each takes 1 unit time to paint 1 unit of board. The problem is to find the minimum time to get
this job done under the constraints that any painter will only paint continuous sections of boards, say board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.
"""


def painters(k, A):
    if k == 1:
        return sum(A)
    if k % 2 == 0:
        left_painter = right_painter = 0
        left_index, right_index = 0, len(A)-1
        while (right_index - left_index) > 0:
            if left_painter < right_painter:
                left_painter += A[left_index]
                left_index += 1
            else:
                right_painter += A[right_index]
                right_index -= 1
        else:
            if left_painter < right_painter:
                return max(painters(k-1, A[left_index + 1:]), painters(k-1, A[:left_index]))
            return max(painters(k-1, A[right_index - 1:]), painters(k-1, A[:right_index]))

        return 0

if __name__ == '__main__':
    k = 2
    A = [10, 10, 10, 10]
    print(painters(k, A))
    k = 2
    A = [10, 20, 30, 40]
    print(painters(k, A))
