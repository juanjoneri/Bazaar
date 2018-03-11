import random


def partition(l, i):
    pivot = l[i]
    left = filter(lambda x: x < pivot, l)
    center = filter(lambda x: x == pivot, l)
    right = filter(lambda x: x > pivot, l)
    return list(left), list(center), list(right)


def quick_sort(l):
    if len(l) <= 1: return l
    pivot_index = int(random.random() * len(l))
    left, center, right = partition(l, pivot_index)
    return quick_sort(left) + center + quick_sort(right)


if __name__ == '__main__':
    a = [1, 2, 4, 3, 4, 1, 0, 6, 11, 4]
    print(quick_sort(a))