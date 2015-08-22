M = 0
for a in range(1, 100):
    for b in range(1, 100):
        n = a**b
        M = max(M, sum(map(int, str(n))))

print(M)
