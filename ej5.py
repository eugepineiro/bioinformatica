import argparse
import os


#argparse with optional input file and pattern
parser = argparse.ArgumentParser()
parser.add_argument("--input", help="input file", type=str, default="fasta/sequence.fas", required=False)
parser.add_argument("--output", help="output file", type=str, default="sequence", required=False)

args = parser.parse_args()

os.system("getorf -sequence " + args.input + " -outseq " + "protein_" + args.output +".orf" + " -find 1")   # Get proteins 
os.system("getorf -sequence " + args.input + " -outseq " + args.output +".orf" + " -find 3")                # Get nucleotide 
os.system("transeq -sequence " + args.input + " -outseq " + args.output + ".pep")                           # Translate sequence 

os.system("patmatmotifs -sequence " + args.input + " -outfile " + args.output + ".patmatmotifs")             # Domain analysis