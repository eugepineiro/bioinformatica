# BLAST 
import os
from Bio.Blast import NCBIWWW
from Bio import SeqIO
import threading
import argparse

def online_blastn(file):
    try:
        filepath = f"{args.input}/{file}" if is_dir(args.input) else args.input
        seq = SeqIO.read(filepath, format="fasta") # Read sequence
    except OSError as e:
        print(f"Error: Unable to open {args.input}: {e}")
        exit(1)
    except ValueError:
        print(f"Error: Can not read {args.input}")
        exit(1)
    try: 
        result = NCBIWWW.qblast("blastn", "nt", seq.seq) # Execute BLASTN to NCBI
    except: 
        print("Error: NCBI Remote blastn failed")
        exit(1)
    # Save blast result for each ORF
    file = file.split(".")[0]
    with open(f"{args.output}{file}.xml", "w") as f:
        print(f"Saving results in {args.output}/{file}.xml")
        f.write(result.read())  

def local_blastp(file):
    # Translate ORF to protein
    try:
        filepath = f"{args.input}/{file}" if is_dir(args.input) else args.input
        record = SeqIO.read(filepath, format="fasta")# Read sequence
    except OSError as e:
        print(f"Error: Unable to open {args.input}: {e}")
        exit(1)
    except ValueError:
        print(f"Error: Can not read {args.input} in fasta format")
        exit(1)
    
    seqprot = record.seq.translate(stop_symbol="")

    # Save protein sequence
    name = file.split(".")[0]
    path = f"{args.output}/{name}_protein.fasta"
    os.makedirs(args.output, exist_ok=True)
    with open(path, "w") as f:
        print(f"Saving results in {path}")
        f.write(f">{record.id}\n")
        f.write(seqprot.__str__())
    
    # Exceute local BLASTP command 
    command = f'blastp -query {path} -db /root/swissprot -outfmt 5 -out blast/{name}.xml'
    try: 
        os.system(command) 
    except:
        print("Error: Local BLASTP failed. Please make sure you've got swissprot database installed")
        exit(1)

def is_file(path):
    return os.path.isfile(path)

def is_dir(path):
    return os.path.isdir(path)

def run_blast(target):
        
        threads = []

        input_path = args.input

        if is_file(input_path):
            print("Running BLAST for single file")
            target(input_path)
            return
        
        if not is_dir(input_path):
            print(f"Error: {input_path} is not a file or directory")
            exit(1)

        files = os.listdir(input_path)
        for file in files:
            print(f"BLAST for file {file}")
            t = threading.Thread(target=target, args=(file,)) # Multithreading to speed up process
            t.start()
            threads.append(t)
    
        for i,t in enumerate(threads):
            try:
                t.join()
            except:
                print(f"Error: BLAST failed for file {files[i]}")



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
        print("Please enter a blastp or blastn method")
        exit(1)
    print(f"Starting {args.method} with {args.input}")
    run_blast(target)