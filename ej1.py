# Procesamiento de Secuencias 
import Bio
from Bio import SeqIO

def genbank_to_fasta(genbank_filename):

    for seq_record in SeqIO.parse(genbank_filename, "genbank"):

        print(seq_record)
        print("ID: %s, Length: %i, with %i features" % (seq_record.id, len(seq_record), len(seq_record.features)))

    count = SeqIO.convert(genbank_filename, "genbank", "sequence.fasta", "fasta")
    print("Converted %i records" % count)


if __name__ == '__main__':
    
    genbank_to_fasta("seq_multiple.gb")