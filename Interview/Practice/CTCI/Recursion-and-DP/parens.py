"""
Implement an algorithm to print all valid combinations of n pairs of parentheses
"""

def valid_parens(n):
    if n == 0:
        yield ''
    else:
        for valid_paren in valid_parens(n-1):
            yield f'(){valid_paren}'
            yield f'({valid_paren})'


def main():
    print(list(valid_parens(3)))

if __name__ == '__main__':
    main()
