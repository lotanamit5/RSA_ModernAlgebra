from random import randrange


def extended_gcd(a, b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    if a == 0:
        return b, 0, 1

    d, x_new, y_new = extended_gcd(b % a, a)

    x = y_new - (b//a) * x_new
    y = x_new

    return d, x, y


def modular_inverse(a, n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    (gcd, c, d) = extended_gcd(a, n)
    if(gcd == 1):
        return c % n

    return None


def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
    # bn = format(int(d), "b")
    d = int(d) % int(n)
    bn = bin(int(d))
    better_a = int(a) % int(n)
    res = 1
    bn = bn[2:]
    bn = bn[::-1]
    for i in range(len(bn)):
        if(bn[i] == '1'):
            exp = 2**i
            exp = int(exp) % int(n)
            a_exp = int(better_a) ** exp
            res *= a_exp % int(n)
            res = res % int(n)
    return res


def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1, n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False


def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True


def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None
