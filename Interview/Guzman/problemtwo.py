# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def get_pairs(connections):
    return [connections[i:i+2] for i in range(0, len(connections), 2)]

def get_longest_subsequence(pairs):
    return

def solution(A, E):
    pairs = get_pairs(E)
    weigth_positions = [[i for i, x in enumerate(A) if x == weight] for weight in set(A)]

    # for each weight, find longest connected subsequence of nodes
    connected_subsequences = []
    for weight_index in range(set(A)):
        # get all the pairs with that weight
        pairs_with_weight = [pairs[i] for i in weight_positions[weight_index]]
        connected_subsequences.extend(get_longest_subsequence(pairs_with_weight)
    # find the longest and return its length
    return len(max(longest_subsequences, key=len))
