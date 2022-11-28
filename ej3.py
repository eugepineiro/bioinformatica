from Bio import SeqIO, AlignIO, Seq, SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio.Align.Applications import MuscleCommandline
import argparse
from enum import Enum
import os


class MSA(Enum):
    CLUSTALW = 1
    MUSCLE = 2
    
def msa(in_file, out_file, method):
  
  if method == MSA.CLUSTALW:
    cline = ClustalwCommandline("clustalw2",infile=in_file, outfile=out_file)

  elif method == MSA.MUSCLE:
    command = f"muscle -align {in_file} -output {out_file}"
    cline = lambda  : os.system(command) 
    
  else: 
    print("Error: Invalida MSA method")
    exit(1)

  try:
    cline()
  except OSError as e:
    print(f"Error: Unable to open {in_file}: {e}")
    exit(1)
    


if "__main__" == __name__:

  parser = argparse.ArgumentParser(prog="ej3.py", description="Execute Multiple Sequence Alignment with Clustawl or Muscle")
  parser.add_argument("--method", help="MSA method (clustalw or muscle)", type=str, required=True, choices=["clustalw", "muscle"])
  parser.add_argument("--input", help="Input file (.fas)", type=str, required=True)
  parser.add_argument("--output", help="Output file", type=str, required=True)

  args = parser.parse_args()
  in_file = args.input
  out_file = args.output

  extension = args.input.split(".")[1]

  if extension != ".fas" or extension != ".fasta": 
    print("Error: Please enter .fas or .fasta file") 
    exit(1)    

  method = MSA.CLUSTALW if args.method == "clustalw" else MSA.MUSCLE
  msa(in_file, out_file, method)