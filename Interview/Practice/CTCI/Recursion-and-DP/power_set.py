"""
Write a method to return all subsets of a set
"""

def subsets(A):
    yield A
    for a in A:
        yield from subsets(A-{a})


def main():
    print(list(subsets({1,2,3})))


if __name__ == '__main__':
    main()
