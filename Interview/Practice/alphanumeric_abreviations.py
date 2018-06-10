"""
Given a string of characters of length less than 10. We need to print all the alpha-numeric abbreviation of the string.

The alpha-numeric abbreviation is in the form of characters mixed with the digits which is equal to the number of skipped characters of a selected substring. So, whenever a substring of characters is skipped, you have to replace it with the digit denoting the number of characters in the substring. There may be any number of skipped substrings of a string. No two substrings should be adjacent to each other. Hence, no two digits are adjacent in the result. For a clearer idea, see the example.

Input : ABC
Output :
ABC
AB1
A1C
A2
1BC
1B1
2C
3
Note: 11C is not valid because no two digits should be adjacent,
2C is the correct one because AB is a substring, not A and B individually
"""

import re

def collapse(word):
    """collapses of adjacent numbers in a word into their sum"""
    pattern = r'\d+'
    number_sections = [(m.start(), m.end()) for m in re.finditer(pattern, word)]
    for start, end in reversed(number_sections):
        equivalent = sum(map(int, word[start:end]))
        word = word[:start] + str(equivalent) + word[end:]

    return word

def alphanumeric_abreviations(remaining, sofar=''):
    """solve the puzzle"""
    for i in range(len(remaining)):
        yield from alphanumeric_abreviations(
            remaining[i+1:], sofar=sofar + remaining[:i] + '1')

    abreviation = collapse(sofar + remaining)
    yield abreviation

if __name__ == '__main__':
    known = set(alphanumeric_abreviations('ABC'))
    print(known)
