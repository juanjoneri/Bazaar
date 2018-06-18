"""
given a list of tuples, return n highest by 2nd element
input: [('jo', 2),('ajo', 3),('spin', -1),('sro', 300),('yo', 0)]
        2
out: 'sro', 'ajo'
"""
from operator import itemgetter

def max_n(tuples, n):
    return list(map(itemgetter(0), sorted(tuples, key=itemgetter(1))[-n:]))

if __name__ == '__main__':
    print(max_n([('jo', 2),('ajo', 3),('spin', -1),('sro', 300),('yo', 0)], 2))
