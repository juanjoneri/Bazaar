'''
1. Choose two different prime numbers `p`, `q`
2. Compute `N` = p*q
3. Compute Eulers `φ(N)` = (p-1)(q-1)
4. Choose encryption exponent `e` s.t GCD(e, φ(N)) = 1 (any prime > φ(N)/2)
5. Compute decryption exponent `d` s.t. e*d % φ(N) = 1
'''

import os
from Crypto.Util import number
from math import ceil, log
from encode import to_number, to_text

# We will use the Euclidean algorithm to find d
def inverse(x, m):
    a, b, u = 0, m, 1
    while x > 0:
        q = b // x
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1: return a % m


def rsa_tool(p, q):
    N = p * q
    phi = (p-1)*(q-1)
    e = number.getPrime(ceil(log(phi/2)), os.urandom)
    d = inverse(e, phi)

    public = (N, e)
    private = (N, d)

    # decrypts a single unit of information smaller than N
    def decrypt(code):
        nonlocal private
        N, d = private
        if code >= N: raise ValueError('Too big to decrypt')
        else: return (code ** d) % N
    
    return public, decrypt

def encrypt(public, message):
    N, e = public
    return message ** e % N

def encrypt_parts(public, message_parts):
    code_parts = []
    for part in message_parts:
        code_parts.append(encrypt(public, part))
    return code_parts

def decrypt_parts(decrypt, code_parts):
    message_parts = []
    for part in code_parts:
        message_parts.append(decrypt(part))
    return message_parts


def test():
    public, decrypt = rsa_tool(311, 499)

    code = encrypt(public, 43)
    assert(decrypt(code) == 43)

    message = 'hellomyfriendthismessageisjustforyou'
    parts = to_number(message, 4)
    code_parts = encrypt_parts(public, parts)
    message_parts = decrypt_parts(decrypt, code_parts)
    assert(to_text(message_parts) == message)


if __name__ == '__main__':
    test()


