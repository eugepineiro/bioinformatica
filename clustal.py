from Bio.Align.Applications import ClustalwCommandline
clustalw_exe = "./clustalw2"
in_file = "./multipleNoGaps.fasta"
out_file = "./alignedClustalNoGaps.fasta"
clustalw_cline = ClustalwCommandline(clustalw_exe, infile=in_file, outfile=out_file)
clustalw_cline()
