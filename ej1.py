# Sequence Processing
from Bio import SeqIO
import os
import argparse
import sys

PROGRAM_ARGUMENTS = 1
CODON_LEN = 3
STOP_CODONS = ["TAA", "TAG", "TGA"]
START_CODON = "ATG"

def genbank_to_fasta(genbank_filename):

    for seq_record in SeqIO.parse(genbank_filename, "genbank"):

         print("ID: %s, Length: %i, with %i features" % (seq_record.id, len(seq_record), len(seq_record.features)))

    return seq_record.seq


def find_codon(seq_record, start, codons):
    for i in range(start, len(seq_record), CODON_LEN):
        codon = seq_record[i:i+CODON_LEN]
        if codon in codons:
            return i
    return -1

def find_with_start_codon(seq_record: str):
     
    start = 0

    start = find_codon(seq_record, start, [START_CODON]) # Devuelve donde comienza el codon en la sequencia
    if start == -1: # No está en la secuencia 
        return ""
    
    end = find_codon(seq_record, start, STOP_CODONS) + CODON_LEN
    
    if end != -1:
       return seq_record[start:end] # La primera seq encontrada que empieza con ATG y termina con "TAA", "TAG", "TGA"
   

def orf_finder(sequence:str): 

    orfs = []
    for i in range(CODON_LEN):
        orfs.append(find_with_start_codon(sequence[i:]))
    #reverse sequence
    sequence = sequence[::-1] 
    for i in range(CODON_LEN):
        orfs.append(find_with_start_codon(sequence[i:]))
    return orfs

if __name__ == '__main__':
    
    # Parse arguments 
    parser = argparse.ArgumentParser(prog="ej1.py", description="Reads one or multiple nucleotide sequences in genbank format (.gb) and saves them in fasta format (.fas)")
    parser.add_argument("--input", help="path to GENBANK input file (.gb)", type=str,  metavar="file.gb", required=True)
    parser.add_argument("--output", help="path to save FASTA output file. Defaults to create a /orf folder", type=str, metavar="path/to/file", default="orf", required=False)
    args = parser.parse_args()
    
    try:
        records = SeqIO.parse(args.input, "genbank") # Parse genbank file
    except OSError as e:
        print(f"Error: Unable to open {args.input}: {e}")
        exit(1)
    except ValueError:
        print(f"Error: Can not read {args.input} as .gb format")
        exit(1)
    # Find ORF for each record in multiple fasta file
    for record in records:

        seq = str(record.seq)
        
        orfs = orf_finder(seq)

        if len(orfs) == 0: 
            print("No ORFs found")
            exit()

        # Save orfs in a file
        dir_name = f"{args.output}/{record.id}/"
        os.makedirs(dir_name, exist_ok=True)        
        for i, orf in enumerate(orfs):

            with open(f"{dir_name}orf{i}_{len(orf)}.fas" , "w") as f:
                f.write(f">{i} Length {len(orf)}\n") # Create sequence ID
                f.write(orf)        