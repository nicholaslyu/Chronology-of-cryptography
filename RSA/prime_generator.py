import random


def nBitRandom(n=1024):
    return(random.randrange(2**(n-1)+1, 2**n-1))




primes_under_1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47, 53, 59, 61, 67,
                    71, 73, 79, 83, 89, 97, 101, 103,
                    107, 109, 113, 127, 131, 137, 139, 
                    149, 151, 157, 163, 167, 173, 179, 
                    181, 191, 193, 197, 199, 211, 223, 
                    227, 229, 233, 239, 241, 251, 257,
                    263, 269, 271, 277, 281, 283, 293,
                    307, 311, 313, 317, 331, 337, 347, 
                    349, 353, 359, 367, 373, 379, 383, 
                    389, 397, 401, 409, 419, 421, 431, 
                    433, 439, 443, 449, 457, 461, 463, 
                    467, 479, 487, 491, 499, 503, 509, 
                    521, 523, 541, 547, 557, 563, 569, 
                    571, 577, 587, 593, 599, 601, 607, 
                    613, 617, 619, 631, 641, 643, 647, 
                    653, 659, 661, 673, 677, 683, 691, 
                    701, 709, 719, 727, 733, 739, 743, 
                    751, 757, 761, 769, 773, 787, 797, 
                    809, 811, 821, 823, 827, 829, 839, 
                    853, 857, 859, 863, 877, 881, 883, 
                    887, 907, 911, 919, 929, 937, 941, 
                    947, 953, 967, 971, 977, 983, 991, 997]

PRIMES_UNDER_1000 = set(primes_under_1000)


def check_small_primes(p,q):
        if p <1000 and q <1000:
                if p in PRIMES_UNDER_1000 and q in PRIMES_UNDER_1000 and p!=q:
                    return p*q
        return None

def generate_1024_prime():
    pq_list = []
    while True:
        num = nBitRandom(20)
        if is_prime(num):
             pq_list.append(num)
        if len(pq_list) == 2:
             break
    return pq_list
    
             

def is_prime(n):
    """Test whether a given number is prime using the Miller-Rabin test.
    n: the number to be tested.
    """
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False

    # Express n - 1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Repeat 40 times
    for _ in range(40):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def pow_mod(p, q, n):
    res = 1
    while q :
        if q & 1:
            res = (res * p) % n
        q >>= 1
        p = (p * p) % n
    return res