def chop(lis, s):
    '''
    chops a list in pieces of size s
    '''
    return [lis[i:i+s] for i in range(0, len(lis), s)]

def to_number(text, size):
    '''
    Turns a text into chunks of size=size groups of decimal numbers
    as mapped by encode.
    ('abcd', 2) -> [encode('a')encode('b'), encode('c')encode('d')]
    '''
    def encode(char):
        '''
        Defines the encoding of a single character
        55 makes A be at 10 and z at 67 so that all characters
        use 2 and only 2 digits
        '''
        return str(ord(char) - 55)

    if len(text) == 0 or size % 2 != 0:
        raise ValueError('size must be a multiple of 2')
    
    encoded = ''.join(map(encode, text))
    return list(map(int, chop(encoded, size)))
    
def to_text(number_sections):
    '''
    Does the opposite of to_number
    '''
    def decode(num):
        return str(chr(num + 55))

    string_sections = map(str, number_sections)
    ans = ''
    for section in string_sections:
        numbers = chop(section, 2)
        ans += ''.join(map(decode, map(int, numbers)))

    return ans


if __name__ == '__main__':
    assert(to_text(to_number('Azcd', 4)) == 'Azcd')
    assert(to_text(to_number('faASDAeASFDa', 6)) == 'faASDAeASFDa')
    text = 'Holacomoestasamigomio'
    assert(to_text(to_number(text, 8)) == text)