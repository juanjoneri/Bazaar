"""
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B
Write a method to merge B into A in sorted order
"""



def sorted_merge(A, B):
    last_b = len(B)-1
    last_a = len(A)-len(B)-1

    for i in reversed(range(len(A))):
        a, b = A[last_a], B[last_b]

        if a > b and last_a != -1:
            last_a -= 1
            A[i] = a
        elif last_b != -1:
            last_b -= 1
            A[i] = b
        else:
            break

    return A


def main():
    A, B = [2, 4, 6, 8, 10, None, None, None, None, None], [1, 3, 5, 7, 9]
    assert sorted_merge(A, B) == list(range(1, 11))

    A, B = [-1, 3, 5 ,13, 1000, 1001, None, None, None, None, None], [-2000, 0, 10 ,1000, 1000000]
    assert sorted_merge(A, B) == [-2000, -1, 0, 3, 5, 10 ,13, 1000, 1000, 1001, 1000000]

if __name__ == '__main__':
    main()
