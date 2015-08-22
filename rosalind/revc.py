#!/usr/bin/env python3

dna_str  = input()
dna_c = dna_str.translate(str.maketrans('ACGT','TGCA'))[::-1]
print(dna_c)

"""
python 2.x用コード
import string

dna_c = dna_str.translate(string.maketrans('ACGT','TGCA'))[::-1]
"""

"""
Biopythonコード(python 2.x)
from Bio import SeqIO
from Bio.Alphabet import NucleotideAlphabet
dna = SeqIO.Seq(raw_input(),NucleotideAlphabet())
print dna.reverse_complement()
"""
