from Bio import SeqIO, AlignIO, Seq, SeqRecord

from Bio.Align import MultipleSeqAlignment
def msa():

    #align = list(AlignIO.parse("fasta/seq_multiple.fas", "fasta"))

    #input_handle = open("test.fasta", "r")
    output_handle = open("msa.fasta", "w")

    alignments = list(AlignIO.parse("test.fasta", "fasta"))



    align = MultipleSeqAlignment(alignments)
    
    #seqs = [ [seq for seq in alignment][0] for alignment in alignments]

    
    # seqs = []

    # for alignment in alignments:
    #     for record in alignment:
    #         print(record.seq)
    #         print(record.id)
    #         seqs.append(record.seq)
      #print(alignment.seq)

    AlignIO.write(alignments, output_handle, "fasta")
 

    output_handle.close()
    #input_handle.close()


if "__main__" == __name__:
    msa()