from utils import get_rand_prime
from random import randrange
from utils import inverse


class RSA(object):
    def __init__(self, bits):
        self.parameters = self.setup(bits)

    def setup(self, nbits=512):
        p = get_rand_prime(nbits)
        q = get_rand_prime(nbits)
        while p == q:
            q = get_rand_prime(nbits)
        n = p * q
        phi = (p-1) * (q-1)
        e = randrange(2**16, 2**17)
        d = inverse(e, phi)
        while d == -1:
            e = randrange(2**16, 2**17)
            d = inverse(e, phi)

        return {
            "p": p,
            "q": q,
            "n": n,
            "phi": phi,
            "e": e,
            "d": d
        }

    def encryption(self, message):
        if self.parameters['n'] == 1:
            return 0
        result = 1
        message = message % self.parameters['n']
        while self.parameters['e'] > 0:
            if self.parameters['e'] % 2 == 1:
                result = (result * message) % self.parameters['n']
            self.parameters['e'] = self.parameters['e'] >> 1
            message = (message * message) % self.parameters['n']
        return result

    def decryption(self, message):
        n = self.parameters['p'] * self.parameters['q']

        # 1- Convert to CRT domain
        yp = message % self.parameters['p']
        yq = message % self.parameters['q']

        # 2- Do the computations
        dp = self.parameters['d'] % (self.parameters['p'] - 1)
        dq = self.parameters['d'] % (self.parameters['q'] - 1)

        xp = pow(yp, dp, self.parameters['p'])
        xq = pow(yq, dq, self.parameters['q'])

        # 3- Inverse transform
        inv = inverse(self.parameters['p'], self.parameters['q'])
        print(inv)
        cp = pow(self.parameters['q'], self.parameters['p'] - 2, self.parameters['p'])
        cq = pow(self.parameters['p'], self.parameters['q'] - 2, self.parameters['q'])

        result = ((self.parameters['q'] * cp * xp) + (self.parameters['p'] * cq * xq)) % n
        return result
