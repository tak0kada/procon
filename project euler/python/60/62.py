from __future__ import division, print_function

def split(i):
    tmp = list(str(i))
    tmp.sort()
    return tmp

sect = [1, 3, 5, 10, 22, 47, 100, 216, 465, 1000, 2155, 4642, 10000, 21545, 46416, 100000]

for i in range(15):
    cube = [i**3 for i in range(sect[i], sect[i+1])]
    cube_split = [split(i) for i in cube]
    for i, sp in enumerate(cube_split):
        if cube_split.count(sp) == 5:
            print(cube[i])
            break
    else:
        continue
    break

