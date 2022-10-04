from Bio.Align.Applications import MuscleCommandline
in_file = "./multiple.fasta"
out_file = "./aligned.fasta"
muscle_cline = MuscleCommandline(input=in_file, out=out_file)
muscle_cline()