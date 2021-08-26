import random


def gcd(a, b):
    # search for the greatest common divider (should be 1)
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def multiplicativeInverse(a, b):
    """Euclid's extended algorithm"""
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa
    return lx


def generatePrime():
    # list of low primes
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
                 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
                 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
                 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
                 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787]
    # select 1 number from list
    num = random.choice(lowPrimes)
    # returning prime number
    return num


def publicKeyGeneration():
    # generating 2 primes
    p = generatePrime()
    q = generatePrime()
    # if they are equal , run again generate prime.
    while p == q:
        p = generatePrime()
        q = generatePrime()
    # calculating necessary parameters for private and public keys
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    publicPQ = p, q
    return (n, e), (p, q)


def privateKeyGeneration(publicKey, p, q):
    n, e = publicKey
    phi = (p - 1) * (q - 1)
    x = multiplicativeInverse(e, phi)
    # returning public and private key
    return x, n


def encryptRSA(publicKey, textToEncrypt):
    # getting public key and separate it to n and e
    n, e = publicKey
    # encrypt text with public key
    encryptedText = [(ord(char) ** e) % n for char in textToEncrypt]
    return encryptedText
