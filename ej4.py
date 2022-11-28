import xml.etree.ElementTree as ET
import argparse


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

if __name__ == '__main__':

    # Parse arguments 
    parser = argparse.ArgumentParser(prog="ej2.py", description="Search pattern in blast output xml file")
    parser.add_argument("--input", help="xml input file to search pattern", metavar="file.xml", type=str,required=True) #default="blast/orf0_2787.fas.xml"
    parser.add_argument("--pattern", help="pattern to search",  metavar="pattern", type=str, required=True)

    args = parser.parse_args() 

    if args.input[-4:] != ".xml": 
        print("Error: Please enter .xml file to search pattern") 
        exit(1)
    find_pattern(args.input, args.pattern)