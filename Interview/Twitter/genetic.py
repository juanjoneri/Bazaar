# word -> GGAAAAAA
# c    -> A

def  findMutationDistance(start, end, bank):
    if end not in bank: return -1
    path_lengths = {word: -1 for word in bank}

    path_q = [] # pop(-1)
    path_q.append(start)
    path_lengths[start] = 0

    while any(path_q):
        current = path_q.pop(-1)
        path_length = path_lengths.pop(current)
        if current == end:
            return path_length

        next_words = nextWords(current, path_lengths)

        for word in next_words:
            path_lengths[word] = path_length + 1
            path_q.append(word)



def nextWords(current_word, path_lengths):
    tokens = {'A', 'C', 'T', 'G'}
    next_words = []

    for i in range(len(current_word)):
        for c in tokens:
            if c != current_word[i]:
                new_word = current_word[:i] + c + current_word[i+1:]
                if new_word in path_lengths: next_words.append(new_word)

    return next_words

if __name__ == '__main__':
    bank = {"GAAAAAAA", "AAGAAAAA", "AAAAGAAA", "GGAAAAAA"}
    print(findMutationDistance("AAAAAAAA", "GGAAAAAA", bank))
