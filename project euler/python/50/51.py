#51
import numpy as np

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k = 3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

 
def h(n, L):
    for i in xrange(10):
        t = ""
        for j, k in enumerate(str(n)):
            if j in L: t += str(i)
            else: t += k
        yield int(t)
 
def g(m, n):
    d = {}
    for i, t in enumerate(str(m)):
        d[t] = d.get(t, [])+[i]
    for k,v in sorted(d.items()):
        if len(v)==n: yield int(k),v

def f():
    for i in xrange(3, 100, 3):
        for n in xrange(i+1, 100):
            P = [s for s in p(10**n) if s>10**(n-1)]
            for j in P:
                for k,L in g(j, i):
                    if k>2: break
                    if L[-1]>=n-1: break
                    t = 0
                    for u in h(j, L):
                        if u not in P: t += 1
                        if t>2: break
                    if t==2: return j

print f()
