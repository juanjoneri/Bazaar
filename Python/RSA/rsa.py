'''
1. Choose two different prime numbers `p`, `q`
2. Compute `N` = p*q
3. Compute Eulers `φ(N)` = (p-1)(q-1)
4. Choose encryption exponent `e` s.t GCD(e, φ(N)) = 1 (any prime > φ(N)/2)
5. Compute decryption exponent `d` s.t. e*d % φ(N) = 1
'''

# We will use the Euclidean algorithm to find d
def inverse(x, m):
    a, b, u = 0, m, 1
    while x > 0:
        q = b // x
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1: return a % m


class RSA:
    def __init__(self, p, q):
        self.N = p * q   # PUBLIC
        self.e = 104681  # PUBLIC
        
        self._phi = (p-1)*(q-1)
        self._d = inverse(self.e, self._phi)
        
    def encrypt(self, message):
        if message > self.N:
            raise ValueError('This number is too big to encrypt')
        return (message ** self.e) % self.N

    def decrypt(self, code):
        return (code ** self._d) % self.N

from encode import to_number, to_text
if __name__ == '__main__':
    rsa = RSA(311, 499)
    assert(rsa.decrypt(rsa.encrypt(1)) == 1)
    assert(rsa.decrypt(rsa.encrypt(64508)) == 64508)
    
    message = 'hellomyfriendthismessageisjustforyou'
    message_parts = to_number(message, 4)
    encrypted_parts = []
    for part in message_parts:
        encrypted_parts.append(rsa.encrypt(part))

    decrypted_parts = []
    for part in encrypted_parts:
        decrypted_parts.append(rsa.decrypt(part))

    assert(to_text(decrypted_parts) == message)

