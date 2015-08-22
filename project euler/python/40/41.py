from itertools import permutations
for i in xrange(9,0,-1):
    L=[str(i) for i in xrange(i,0,-1)]
    for j in permutations(L):
        n=int("".join(j))
        if isPrime(n):
            print n
            raise IOError
