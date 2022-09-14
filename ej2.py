# BLAST 
import os
from Bio.Blast import NCBIWWW
import threading

def blast(file):
    #open file
    with open("orf/" + file, "r") as f:
        #read file
        seq = f.read()
        #blast seq
        result = NCBIWWW.qblast("blastn", "nt", seq)
        #save blast result
        with open("blast/" + file + ".xml", "w") as f:
            f.write(result.read())#iterate over dir


threads = []

for file in os.listdir("orf"):
    #create thread
    t = threading.Thread(target=blast, args=(file,))
    #start thread
    t.start()
    #add thread to list
    threads.append(t)

for t in threads:
    #wait for thread to finish
    t.join()


