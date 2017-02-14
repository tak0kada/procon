from __future__ import absolute_import, division, print_function
import numpy as np

def isprime0(n):
    """
    Checks if input n is a prime.
    
    Note
    ----
    a simple implementation of isprime for one-time prime check.
    O(n^2/log(n)) time needed if used many times.
    
    See Also
    --------
    isprime
    """
    #
    if n in (2, 3):
        return True
    if n <= 1 or (n % 6 in (0, 2, 3, 4)):
        return False
    #
    import numpy as np
    sieve = np.ones(n // 3, dtype=np.bool)
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            prime = (3 * i + 4) | 1
            step_ind = 2 * prime
            sieve[prime // 3 + step_ind - 1::step_ind] = False
            sieve[(5 * prime) // 3 - 1::step_ind] = False
    return sieve[-1]

def isprime(n, sieve=[], max=4):
    """
    Checks if input n is a prime.
    
    Note
    ----
    Do NOT set any parameters to sieve and max!
    isprime1 is a more complex implementation of isprime0.
    O(n/log(n)) time needed.
    
    See Also
    --------
    isprime0
    """
    #
    if n in (2, 3):
        return True
    elif n <= 1 or (n % 6 in (0, 2, 3, 4)):
        return False
    #
    elif n <= max:
        return sieve[n // 3 - 1]
    #
    import numpy as np
    sieve = np.ones((2 * n) // 3, dtype=np.bool)
    for i in range(int(n**0.5) // 3 + 1):
        if sieve[i]:
            prime = (3 * i + 4) | 1
            step_ind = 2 * prime
            sieve[prime//3 + step_ind - 1::step_ind] = False
            sieve[(5 * prime)//3 - 1::step_ind] = False
    max = 2 * n
    return sieve[-1]

def isprime_not_over(n):
    """
    Return the function that checks if input is a prime.

    Parameters
    ----------
    n: int
    
    Returns
    ------
    out: function (isprime)

    Example
    -------
    >>> isprime = isprime_not_over(100)
    >>> isprime(71)
    False
    >>> isprime(10000)
    ValueError('Input size over 100')
    """
    if n > 4:
        import numpy as np
        sieve = np.ones(n // 3, dtype=np.bool)
        for i in range(int(n**0.5) // 3 + 1):
            if sieve[i]:
                prime = (3 * i + 4) | 1
                step_ind = 2 * prime
                sieve[prime//3 + step_ind - 1::step_ind] = False
                sieve[(5 * prime)//3 - 1::step_ind] = False

    def isprime(k):
        if k > n:
            raise ValueError("Input size over %d" % n)
        elif k in (2, 3):
            return True
        elif k <= 1 or (k % 6 in (0, 2, 3, 4)):
            return False
        else:
            return sieve[k // 3 - 1]

    return isprime

def primesfrom2under(n):
    """
    Return the ndarray of primes from 2 to under n.
    """
    sieve = np.ones(n // 3 + (n % 6 == 2) - 1, dtype=np.bool)
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            prime = (3 * i + 4) | 1
            step_ind = 2 * prime
            sieve[prime//3 + step_ind - 1::step_ind] = False
            sieve[(5 * prime)//3 - 1::step_ind] = False
    primes_over_5 = (3 * np.nonzero(sieve)[0] + 4) | 1
    primes = np.hstack([[2,3], primes_over_5])
    return primes
