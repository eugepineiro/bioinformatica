import xml.etree.ElementTree as ET
import argparse
from Bio import Entrez
import os

def find_pattern(file, pattern):

    print(f"Searching for pattern {pattern} in {file}...")

    #Parse XML file
    try:
        tree = ET.parse(file)
    except OSError as e:
        print(f"Error: Unable to open {file}: {e}")
        exit(1)
    
    root = tree.getroot()
    iteration_hits = root.findall("BlastOutput_iterations/Iteration/Iteration_hits")
    if len(iteration_hits) == 0:
        print("Error: XML file is not a BLAST output")
        exit(1)
        
    hits = iteration_hits[0].findall("Hit")
    if(len(hits) == 0): 
        print("XML has no hits")
        exit(1)

    matched = []

    # Search pattern in hits
    for hit in hits:
        if pattern.lower() in hit.find("Hit_def").text.lower():
            matched.append((hit.find("Hit_def").text, hit.find("Hit_accession").text))
            
    if(len(matched) == 0): 
        print(f"Pattern {pattern} not found in {file}")
        exit()
    else: 
        print(f"Found {len(matched)} matches")
        for match in matched:
            print(f"{match}\n")
        return matched

def search_by_accession(dir_name, query):
    Entrez.email = 'A.N.Other@example.com'
    fasta = Entrez.efetch(db="nucleotide", id=query, rettype="fasta")
    # Save fasta in a file   
    try: 
        with open(f"{dir_name}/{query}.fas" , "w") as f:
            f.write(f"{fasta.read()}") # Create sequence ID
    except OSError as e:
        print(f"Error: Unable to write {dir_name}/{query}.fas: {e}")
        exit(1)      
        
        
if __name__ == '__main__':

    # Parse arguments 
    parser = argparse.ArgumentParser(prog="ej4.py", description="Search pattern in blast output xml file and find fasta from accession number")
    parser.add_argument("--input", help="xml input file to search pattern", metavar="file.xml", type=str,required=True) #default="blast/orf0_2787.fas.xml"
    parser.add_argument("--pattern", help="pattern to search",  metavar="pattern", type=str, required=True)
    parser.add_argument("--search", help="if true, get sequences from NCBI", action="store_true", required=False)
    parser.add_argument("--output", help="output directory for sequences", type=str, default="entrez-sequences", required=False)

    args = parser.parse_args() 

    # Search Pattern 
    if args.input[-4:] != ".xml": 
        print("Error: Please enter .xml file to search pattern") 
        exit(1)
    
    hits = find_pattern(args.input, args.pattern)

    # Search by accession 
    if args.search:
        os.makedirs(args.output, exist_ok=True)
        for hit in hits:
            print(f"Searching for {hit[1]} in NCBI...")
            search_by_accession(args.output, hit[1]) # Cant do multithreading cause NCBI does not accept too many requests