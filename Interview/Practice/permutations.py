"""
Return all permutations of a given set
"""


def permute(remaining, sofar=''):
    if not any(remaining):
        print(sofar)

    for i in range(len(remaining)):
        left = sofar + remaining[i]
        right = remaining[:i] + remaining[i+1:]
        permute(right, sofar=left)

if __name__ == '__main__':
    permute('abc')
