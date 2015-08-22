from __future__ import division, print_function
from itertools import permutations

t = [[i*(i+1)//2    for i in range(200) if 1000 <= i*(i+1)//2   < 10000],
     [i**2          for i in range(100) if 1000 <= i**2         < 10000],
     [i*(3*i-1)//2  for i in range(90)  if 1000 <= i*(3*i-1)//2 < 10000],
     [i*(2*i-1)     for i in range(80)  if 1000 <= i*(2*i-1)    < 10000],
     [i*(5*i-3)//2  for i in range(70)  if 1000 <= i*(5*i-3)//2 < 10000],
     [i*(3*i-2)     for i in range(60)  if 1000 <= i*(3*i-2)    < 10000]]

T = [[[], []], [[], []], [[], []], [[], []], [[], []], [[], []]]

def sep(T):
    for i in range(6):
        for j in t[i]:
            s0, s1 = str(j)[:2], str(j)[2:]
            T[i][0].append(s0)
            T[i][1].append(s1)

def seggraph(idt, p, q):
    tr = [T[p][1][i] for i in idt[p]]
    idt[q] = [i for i in idt[q] if T[q][0][i] in tr]
    tr = [T[q][0][i] for i in idt[q]]
    idt[p] = [i for i in idt[p] if T[p][1][i] in tr]

def graph(order):
    idt = [[i for i in range(len(t[j]))] for j in range(6)]
    for time in range(3):
        for i in range(6):
            seggraph(idt, *order[i:i+2])
    if idt[0]:
        return [i[0] for i in idt]

sep(T)

for p in permutations(range(1, 6)):
    order = (0,) + p + (0, )
    idt = graph(order)
    if idt:
        print(order)
        print([t[i][idt_] for i, idt_ in enumerate(idt)])

