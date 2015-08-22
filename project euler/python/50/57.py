#numerator: n
#denominator: d

diff = 0
n, d = 1, 1
for i in range(1000):
    n, d = n + 2*d, n + d
    diff += len(str(n)) - len(str(d))

print(diff)
