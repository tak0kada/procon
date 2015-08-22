from __future__ import division
import numpy as np
from itertools import combinations
from sympy import factorint

def product(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p

def phi(n):
    factor = list(factorint(n))
    
    phi = n
    for i in range(1, len(factor) +1):
        for j in combinations(factor, i):
            phi += (-1) ** i * (n // product(j))
    return phi

def ispermutation(n, m):
    n, m = list(str(n)), list(str(m))
    n.sort()
    m.sort()
    if n == m:
        return True
    else:
        return False

m = (10, 0)
for i in range(2, 10**7):
    p = phi(i)
    if ispermutation(p, i) and i / p < m[0]:
            m = (i / p, i)

print(m)
