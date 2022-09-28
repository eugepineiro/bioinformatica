# Import libraries
from Bio import pairwise2
from Bio.Seq import Seq
 
# Creating sample sequences
seq1 = Seq("TGTGACTA")
seq2 = Seq("CATGGTCA")
 
# Finding similarities
alignments = pairwise2.align.globalxx(seq1, seq2)
 
# Showing results
for match in alignments:
    print(match)