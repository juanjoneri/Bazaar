"""
Write a method to srot an array of strings so that all the anagrams are next to each other
abc - bca - acb are anagramas
"""
from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        groups[''.join(sorted(word))].append(word)

    return list(groups.values())


def main():
    print(group_anagrams(['abc', 'def', 'bac', 'acb', 'fed', 'dfe']))


if __name__ == '__main__':
    main()
