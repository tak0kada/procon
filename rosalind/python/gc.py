#! /usr/bin/env/python3

import sys

rawdata = sys.stdin.read().split('\n')
ID, dna = [], []

i = 0
while i < len(rawdata):
    if rawdata[i] == '':
        break
    if rawdata[i][0] == '>':
        ID.append(rawdata[i][1:])
        dna.append("")
    else:
        dna[-1] += rawdata[i]
    i += 1

gc = [100*(i.count('G')+i.count('C'))/len(i) for i in dna]
index = gc.index(max(gc))

print(ID[index]+'\n'+str(round(gc[index], 4)))
