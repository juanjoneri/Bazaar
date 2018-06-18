"""
Given a set, find the subset of that set that maximizes sum
"""


from collections import namedtuple




def max_sum(A):
    PartialSolution = namedtuple('PartialSolution', ['best_including', 'best_excluding'])

    def partial_sum(A):
        last = A[-1]
        if len(A) == 1:
            best_including = last
            best_excluding = 0

        else:
            best_including = max(last, partial_sum(A[:-1]).best_including + last)
            best_excluding = max(partial_sum(A[:-1]))

        return PartialSolution(best_including, best_excluding)

    return max(partial_sum(A))



def main():
    assert max_sum([1, 2, -3, 4]) == 4
    assert max_sum([1, 2, -3, 4, 5]) == 9
    assert max_sum([1, 2, -3, 4, -1]) == 4
    assert max_sum([1, 2, -3, 4, -1, 3]) == 6
    assert max_sum([1, -1]) == 1

if __name__ == '__main__':
    main()
