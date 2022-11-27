from Bio.Align.Applications import MuscleCommandline
in_file = "./msa/multipleGaps.fasta"
out_file = "./aligned_multipleGaps.fasta"
muscle_cline = MuscleCommandline(input=in_file, out=out_file)
muscle_cline()