# BLAST 

from Bio.Blast import NCBIWWW

fasta_string = open("orf/orf0_2787.fas").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
#save the blast result
save_file = open("blast/orf0_2787.xml", "w")
save_file.write(result_handle.read())
save_file.close()