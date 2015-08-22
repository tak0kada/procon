from __future__ import division

el = [2] + [(i // 3 + 1) * 2 if i % 3 == 1 else 1 for i in range(99)]

def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        return gcd(min(a, b), max(a, b) % min(a, b))

n, d = el[-1], 1
for i in reversed(el[:-1]):
    n, d = d + n * i, n
    g = gcd(n, d)
    n, d = n // g, d // g

print(sum(map(int, str(n))))
