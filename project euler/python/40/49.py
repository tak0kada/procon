import itertools

def isPrime(n):
    """ignore 2: 4-digit primes don't include 2"""
    if n%2==0: return 0
    else:
        for i in xrange(1,n//4+1):
            if n%(2*i+1)==0: return 0
        else: return 1

def f(L):
    for i in xrange(len(L)):
        for j in xrange(i+1,len(L)):
            if 2*L[j]-L[i] in L:
                print "%i%i%i,D=%i" % (L[i],L[j],2*L[j]-L[i],L[j]-L[i])
for j in xrange(1,10):
    for i in itertools.combinations(range(1,10),3):
        L=[1000*t[0]+100*t[1]+10*t[2]+j for t in itertools.permutations(i) if isPrime(1000*t[0]+100*t[1]+10*t[2]+j)]
        f(L)
