from __future__ import division, print_function
import numpy as np
from itertools import combinations
from mytools import primesfrom2under, isprime_not_over

def concat_isprime(i, j):
    si, sj = str(i), str(j)
    return isprime(int(si + sj)) and isprime(int(sj + si))

def areprime_with(tuple, p):
    for i in tuple:
        if not concat_isprime(i, p):
            return False
    else:
        return True

n = 10000
primes = primesfrom2under(n)
isprime = isprime_not_over(int(str(n)*2))

#primes that are p % 6 == 5 don't satisfy the restriction
p1 = np.hstack([3, primes[primes % 6 == 1]])
p2, p3, p4, p5 = [], [], [], []

for i in range(p1.size):
    for j in p4:
        if areprime_with(j, p1[i]):
            p5= j + (p1[i],)
            break
        else:
            continue
        break
    for j in p3:
        if areprime_with(j, p1[i]):
            p4.append(j + (p1[i],))
    for j in p2:
        if areprime_with(j, p1[i]):
            p3.append(j + (p1[i],))
    for j in p1[:i]:
        if concat_isprime(j, p1[i]):
            p2.append((j, p1[i]))

print(p5)

