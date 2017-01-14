dna1 = input()
dna2 = input()

d = 0
for i,j in zip(dna1, dna2):
    if i != j:
        d += 1

print(d)
