import xml.etree.ElementTree as ET
import argparse


def find_pattern(file, pattern):

    print(f"Searching for pattern {pattern} in {file}")

    #Parse XML file
    try:
        tree = ET.parse(file)
    except OSError as e:
        raise Exception(f"Unable to open {file}: {e}")
    
    root = tree.getroot()
    hits = root.findall("BlastOutput_iterations/Iteration/Iteration_hits/Hit")

    matched = []

    # Search pattern in hits
    for hit in hits:
        if pattern.lower() in hit.find("Hit_def").text.lower():
            matched.append((hit.find("Hit_def").text, hit.find("Hit_accession").text))
            
    if(len(matched) == 0): 
        print(f"Pattern {pattern} not found in {file}")
    else: 
        print(matched)

if __name__ == '__main__':

    # Parse arguments 
    parser = argparse.ArgumentParser(prog="ej2.py", description="Search pattern in blast output xml file")
    parser.add_argument("--input", help="xml input file to search pattern", metavar="file.xml", type=str,required=True) #default="blast/orf0_2787.fas.xml"
    parser.add_argument("--pattern", help="pattern to search",  metavar="pattern", type=str, required=True)

    args = parser.parse_args() 

    if args.input[-4:] != ".xml": 
        raise Exception("Please enter .xml file to search pattern") 
    
    find_pattern(args.input, args.pattern)