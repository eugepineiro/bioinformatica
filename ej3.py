from Bio import SeqIO, AlignIO, Seq, SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio.Application import ApplicationError
from Bio.Align.Applications import MuscleCommandline
import argparse
from enum import Enum
import subprocess
from shutil import which

class MSA(Enum):
    CLUSTALW = 1
    MUSCLE = 2

def isMethodInstalled(method):
  if method == MSA.CLUSTALW:
    return which("clustalw") is not None
  elif method == MSA.MUSCLE:
    return which("muscle") is not None
  else:
    return False

def msa(in_file, out_file, method):
  
  if method == MSA.CLUSTALW:
    cline = ClustalwCommandline("clustalw",infile=in_file, outfile=out_file)

  elif method == MSA.MUSCLE:
    command = ["muscle", "-align", in_file, "-output", out_file]
    cline = lambda  : subprocess.run(command, check=True) 
    
  else: 
    print("Error: Invalid MSA method")
    exit(1)

  try:
    if not isMethodInstalled(method):
      print(f"Error: Unable to run {method.name}. Make sure is installed")
      exit(1)
    cline()
  except ApplicationError:
    print(f"Error: Unable to run {method.name}. Make sure is installed")
    exit(1)
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

  extension = args.input.split(".")[-1]
  if extension != "fas" and extension != "fasta": 
    print("Error: Please enter .fas or .fasta file") 
    exit(1)    

  method = MSA.CLUSTALW if args.method == "clustalw" else MSA.MUSCLE
  msa(in_file, out_file, method)