from Bio.Align.Applications import MuscleCommandline
muscle_exe = "./muscle"
in_file = "./multiple.fasta"
out_file = "./aligned.fasta"
muscle_cline = MuscleCommandline(muscle_exe, input=in_file, out=out_file)
muscle_cline()