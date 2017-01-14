#!/usr/bin/env python3 

dna_string = input()
nucleotide = ('A','C','G','T')
for nt in nucleotide:
    print(dna_string.count(nt), end = " ")
