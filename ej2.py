# BLAST 
import os
from Bio.Blast import NCBIWWW
from Bio import SeqIO
import threading


orf_directory = "orf/NM_000321.3/"
protein_directory = "protein/orf/NM_000321.3/"
os.makedirs(protein_directory, exist_ok=True)

def online_blastn(file):

    seq = SeqIO.read(orf_directory + file, format="fasta")
  
    #blast seq
    result = NCBIWWW.qblast("blastn", "nt", seq.seq)
    #save blast result
    file = file.split(".")[0]
    with open("blast/nuc_" + file + ".xml", "w") as f:
        f.write(result.read())#iterate over dir




def local_blastp(file):
    #translate orf to protein
    record = SeqIO.read(orf_directory + file, format="fasta")
    seqprot = record.seq.translate(stop_symbol="")
    #save protein sequence
    name = file.split(".")[0]
    
    path = f"{protein_directory}{name}_protein.fasta"
    with open(path, "w") as f:
        f.write(f">{record.id}\n")
        f.write(seqprot.__str__())
    command = f'blastp -query {path} -db /root/swissprot -outfmt 5 -out blast/{file}.xml'

    os.system(command)

def run_blast(target):
    
        threads = []
    
        for file in os.listdir(orf_directory):
            #create thread
            t = threading.Thread(target=target, args=(file,))
            #start thread
            t.start()
            #add thread to list
            threads.append(t)
    
        for t in threads:
            #wait for thread to finish
            t.join()



if __name__ == '__main__':

    run_blast(local_blastp)
    