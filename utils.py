from random import randrange


def inverse(e, phi):
    if e > phi :
        e, phi = phi, e
    a, b, u = 0, phi, 1
    while e > 0:
        q = b // e
        e, a, b, u = b % e, u, e, a-q*u
    if b == 1:
        return a % phi
    else:
        return -1


def convert_m2i(msg):
    int_msg = ""
    for ch in msg:
        # pre = "{0:b}".format(ord(ch))
        # if len(pre) < 7:
        #     pre = "0" * (7 - len(pre)) + pre
        pre = bin(ord(ch))
        pre = pre[2:]
        while len(pre) % 8 != 0:
            pre = "0" + pre
        print(pre)
        int_msg += pre
        print(int_msg)
    return int(int_msg, 2)

def convert_i2m(i):
    # bin_format = "{0:7b}".format(i)
    bin_format = bin(i)
    print(bin_format)
    bin_format = bin_format[2:]
    print(bin_format)
    while len(bin_format) % 8 != 0:
        bin_format = "0" + bin_format
    msg = ""
    for b in range(0, len(bin_format), 8):
        msg += chr(int(bin_format[b:b + 8], 2))

    return msg


def millerRabin(p, s):
    r = p - 1
    q = 0
    while r % 2 == 0:
        r = r // 2
        q += 1
    for trials in range(s):
        a = randrange(2, p - 1)
        res = pow(a, r, p)
        if res != 1:
            i = 0
            while res != (p - 1):
                if i == q - 1:
                    return False
                else:
                    i = i + 1
                    res = (res ** 2) % p
    return True


def isPrime(p):
    if (p < 2):
        return False
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                 211, 223, 227,
                 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
                 349, 353, 359,
                 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479,
                 487, 491, 499,
                 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
                 641, 643, 647,
                 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
                 797, 809, 811,
                 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
                 953, 967, 971,
                 977, 983, 991, 997]

    if p in lowPrimes:
        return True

    for prime in lowPrimes:
        if p % prime == 0:
            return False
    return millerRabin(p, 100)


def get_rand_prime(nbits=512):
    while True:
        p = randrange(2 ** nbits, 2 * 2 ** nbits)
        if isPrime(p):
            return p


