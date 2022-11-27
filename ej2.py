# BLAST 
import os
from Bio.Blast import NCBIWWW
from Bio import SeqIO
import threading
import argparse

#orf_directory = "orf/NM_000321.3/"
#protein_directory = "protein/orf/NM_000321.3/"
def online_blastn_old(file):
    print("online blastn for " + file)
    #open file
    with open(args.input + file, "r") as f:
        #read file
        seq = f.read()
        #blast seq
        result = NCBIWWW.qblast("blastn", "nt", seq)
        #save blast result
        with open("blast/nuc_" + file + ".xml", "w") as f:
            f.write(result.read())#iterate over dir


def online_blastn(file):
    try:
        seq = SeqIO.read(args.input + file, format="fasta") # Read sequence
    except OSError as e:
        raise Exception(f"Unable to open {args.input}: {e}")
    except ValueError:
        raise Exception(f"Can not read {args.input}")
    
    try: 
        result = NCBIWWW.qblast("blastn", "nt", seq.seq) # Execute BLASTN to NCBI
    except: 
        raise Exception("NCBI Remote blastn failed")

    # Save blast result for each ORF
    file = file.split(".")[0]
    with open(f"{args.output}{file}.xml", "w") as f:
        print(f"Saving results in {args.output}/{file}.xml")
        f.write(result.read())  

def local_blastp(file):
    # Translate ORF to protein
    try:
        record = SeqIO.read(args.input + file, format="fasta")# Read sequence
    except OSError as e:
        raise Exception(f"Unable to open {args.input}: {e}")
    except ValueError:
        raise Exception(f"Can not read {args.input} in fasta format")
    
    seqprot = record.seq.translate(stop_symbol="")

    # Save protein sequence
    name = file.split(".")[0]
    path = f"{args.output}/{name}_protein.fasta"
    with open(path, "w") as f:
        print(f"Saving results in {path}")
        f.write(f">{record.id}\n")
        f.write(seqprot.__str__())
    
    # Exceute local BLASTP command 
    command = f'blastp -query {path} -db /root/swissprot -outfmt 5 -out blast/{name}.xml'
    try: 
        os.system(command) 
    except:
        raise Exception("Local BLASTP failed. Please make sure you've got swissprot database installed")

def run_blast(target):
    
        threads = []
    
        for file in os.listdir(args.input):
            print(f"BLAST for file {file}")
            t = threading.Thread(target=target, args=(file,)) # Multithreading to speed up process
            t.start()
            threads.append(t)
    
        for t in threads:
            t.join()  # Wait for thread to finish



if __name__ == '__main__':

    # Parse arguments 
    parser = argparse.ArgumentParser(prog="ej2.py", description="Executes BLAST query using NCBI database")
    parser.add_argument("--input", help="path to the sequence to BLAST", type=str,  metavar="path/to/file", required=True)
    parser.add_argument("--output", help="path to folder to save BLAST output in .xml format. Defaults to create a /blast_output folder", type=str, metavar="path/to/file", default="blast_output", required=False)
    parser.add_argument("--method", help="blastn or blastp. Defaults to blastn, blastp requires local swissprot database", type=str, metavar="blastn|blastp", default="blastn", required=False, choices=["blastn", "blastp"])
      
    args = parser.parse_args()
     
    if args.method == "blastn": 
        target=online_blastn
    elif args.method == "blastp": 
        target=local_blastp
    else: 
        raise Exception("Please enter a blastp or blastn method")

    print(f"Starting {args.method} with {args.input}")
    run_blast(target)