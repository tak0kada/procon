from __future__ import division

def diag(edge):
    m = (edge - 2) ** 2
    for i in range(1, 5):
        yield m + (edge - 1) * i

def count_diag_prime(edge):
    diag_bool = [is_prime(i) for i in diag(edge)]
#    print(diag_bool)
    return sum(diag_bool)

#to aboid n_odd / (2 * edge - 1) = 0 at edge = 1,
#edge inits at 3
n_odd, edge = 0, 3
while True:
    n_odd += count_diag_prime(edge)
    if n_odd / (2 * edge - 1) < 0.1:
        print(edge)
        break
    edge += 2

