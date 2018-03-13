from sys import stdin

def is_subset(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

def get_windows(l, window_size):
    nb_windows = len(l) - window_size + 1
    return [tuple(l[i:i+window_size]) for i in range(nb_windows)]

def number_of_conditioned_subranges(upvotes, window_size, condition):
    main_windows = get_windows(upvotes, window_size)
    nb_windows = len(main_windows)
    count = [0] * nb_windows
    for size in range(2, window_size + 1):
        subranges = set(get_windows(upvotes, size))
        for subrange in subranges:
            if all(condition(x, y) for x, y in zip(subrange, subrange[1:])):
                for i in range(nb_windows):
                    if is_subset(subrange, main_windows[i]):
                        count[i] += 1

    return count
    

def str_diff(l, r):
    return [str(a - b) for a, b in zip(l, r)]

if __name__ == '__main__':
    N, K = tuple(map(int, stdin.readline().split()))
    upvotes = list(map(int, stdin.readline().split()))
    non_increasing = number_of_conditioned_subranges(upvotes, K, lambda x, y: x >= y)
    non_decreasing = number_of_conditioned_subranges(upvotes, K, lambda x, y: x <= y)
    print('\n'.join(str_diff(non_decreasing, non_increasing)))