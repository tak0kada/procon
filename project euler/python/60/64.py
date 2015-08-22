from __future__ import division
import numpy as np

def gcd2(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        return gcd2(min(a, b), max(a, b) % min(a, b))

def gcd3(a, b, c):
    return gcd2(gcd2(a, b), gcd2(b, c))

count = 0
for i in range(1, 10001):
    if round(np.sqrt(i)) ** 2 == i:
        continue

    a0, b0, d0 = 1, int(np.sqrt(i)), 1
    a, b, d = a0, b0, d0

    rep = 0
    while True:
        tmp = (a * d * np.sqrt(i) + b * d) / (a ** 2 * i - b ** 2)
        a, b, d = a * d, int(tmp) * (a ** 2 * i - b ** 2) - b * d, a ** 2 * i - b ** 2
        g = gcd3(a, b, d)
        a, b, d = a // g, b // g, d // g
        rep += 1
        
        if (a, b, d) == (a0, b0, d0):
            break

    if rep % 2 == 1:
        count += 1

print(count)
