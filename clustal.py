from Bio.Align.Applications import ClustalwCommandline
in_file = "./multiplep.fasta"
out_file = "./alignedClustal.fasta"
clustalw_cline = ClustalwCommandline("clustalw2",infile=in_file, outfile=out_file)
clustalw_cline()