from Bio.Align.Applications import ClustalwCommandline
in_file = "./msa/multipleGaps.fasta"
out_file = "./alignedClustalmultipleGaps.fasta"
clustalw_cline = ClustalwCommandline("clustalw2",infile=in_file, outfile=out_file)
clustalw_cline()