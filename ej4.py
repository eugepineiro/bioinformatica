import xml.etree.ElementTree as ET
import argparse



#argparse with optional input file and pattern
parser = argparse.ArgumentParser()
parser.add_argument("--input", help="input file", type=str, default="blast/orf0_2787.fas.xml", required=False)
parser.add_argument("--pattern", help="pattern to search", type=str, default="Rattus", required=False)

args = parser.parse_args()

input_file = args.input
pattern = args.pattern

#read xml file
tree = ET.parse(input_file)
root = tree.getroot()
hits = root.findall("BlastOutput_iterations/Iteration/Iteration_hits/Hit")

matched = []

#search pattern in hits
for hit in hits:
     if pattern.lower() in hit.find("Hit_def").text.lower():
         matched.append((hit.find("Hit_def").text, hit.find("Hit_accession").text))

print(matched)


