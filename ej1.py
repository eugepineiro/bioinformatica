# Procesamiento de Secuencias 
from ast import Return
from Bio import SeqIO, AlignIO, Seq
from pprint import pprint

CODON_LEN = 3
STOP_CODONS = ["TAA", "TAG", "TGA"]
START_CODON = "ATG"

def genbank_to_fasta(genbank_filename):

    for seq_record in SeqIO.parse(genbank_filename, "genbank"):

         #print(seq_record)
         print("ID: %s, Length: %i, with %i features" % (seq_record.id, len(seq_record), len(seq_record.features)))
    filename = genbank_filename.split(".")[0] + ".fas"
    count = SeqIO.convert(genbank_filename, "genbank", filename, "fasta")
    print("Converted %i records" % count)

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
       
    try:
        seq = genbank_to_fasta("sequence.gb")
        ##seq to stirng
        seq = str(seq)
        
        orfs = orf_finder(seq)

        for i, orf in enumerate(orfs):
            #save orfs in a file
            with open(f"orf{i}_{len(orf)}.fas" , "w") as f:
                f.write(f">{i} Length {len(orf)}\n")
                f.write(orf)


        pprint(orfs)
        orfs.sort(key= len, reverse=True)
        pprint(list(map(len, orfs)))
        ##pprint()
    except Exception as e:
        print(e)


        