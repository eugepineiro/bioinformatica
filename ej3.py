from Bio import SeqIO, AlignIO, Seq, SeqRecord

def msa():

    #align = list(AlignIO.parse("fasta/seq_multiple.fas", "fasta"))

    input_handle = open("fasta/seq_multiple.fas", "rU")
    output_handle = open("msa.fasta", "w")

    alignments = AlignIO.parse(input_handle, "fasta")
    AlignIO.write(alignments, output_handle, "fasta")

    output_handle.close()
    input_handle.close()

msa()