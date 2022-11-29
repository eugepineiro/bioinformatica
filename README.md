# Bioinformática 

## Análisis de Retinoblastoma Gen RB1

### Integrantes 
- Corfdir, Yohann                     
- Jerusalinsky, Agustín	 
- Piñeiro, Eugenia Sol		 
- Quesada, Francisco 

### Requerimientos 
```
Python3 
Clustalw
Muscle
Blast 
```
Para instalar los modulos de Python necesarios ejectuar el siguiente comando:
```
pip install requeriments.txt
```

Se puede ejecutar el programa en Docker que cuenta con Muscle, Clustalw, BLAST con Swissprot y Emboss con Prosite.
```
make docker
make run
make start
```

### Procesamiento de Secuencias 

Para leer una o múltiples secuencias de nucleótidos de un archivo en formato Genbank (input.gb) y guardaarlas en un archivo FASTA. (output.fas)
```
usage: ej1.py [-h] --input file.gb [--output path/to/file]

Reads one or multiple nucleotide sequences in genbank format (.gb) and saves them in fasta format (.fas)

optional arguments:
  -h, --help            show this help message and exit
  --input file.gb       path to GENBANK input file (.gb)
  --output path/to/file path to save FASTA output file. Defaults to create a /orf folder
```
Ejemplo de ejecución
```
python3 ./ej1.py --input genbank/sequence.gb --output "orfs"
```
### BLAST 

Para ejecutar la consulta de BLAST y obtener los 6 marcos de lectura ejecutar: 

```
usage: ej2.py [-h] --input path/to/file [--output path/to/file] [--method blastn|blastp]

Executes BLAST query using NCBI database

optional arguments:
  -h, --help            show this help message and exit
  --input path/to/file  path to the sequence to BLAST
  --output path/to/file path to folder to save BLAST output in .xml format. Defaults to create a /blast_output folder
  --method blastn|blastp execute blastn or blastp. Defaults to blastn (online), blastp requires local swissprot database

```
Ejemplo de ejecución para un archivo y un directorio con multiples archivos .fas
```
python3 ./ej2.py --input orf/NM_000321.3/orf2_147.fas --output blast_results --method blastn 
python3 ./ej2.py --input orf/NM_000321.3 --output blast_results --method blastp 
```

### MSA

Para ejectuar Multiple Sequence Alignment con Muscle ejecutar:
```
./ej3.py --input msa/multipleGaps.dnd --output msa/alignedmultipleGapsMuscle --method muscle 
```
Para ejectuar Multiple Sequence Alignment con Clustawl ejecutar
```
python3 ej3.py --input msa/multipleGaps.fasta --output msa/alignedmultipleGapsMuscle --method clustalw 
```

### Pattern Matching 
Buscar un patrón dentro de un resultado de BLAST

```
usage: ej4.py [-h] --input file.xml --pattern pattern [--search] [--output OUTPUT]

Search pattern in blast output xml file and find fasta from accession number

optional arguments:
  -h, --help         show this help message and exit
  --input file.xml   xml input file to search pattern
  --pattern pattern  pattern to search
  --search           if true, get sequences from NCBI
  --output OUTPUT    output directory for sequences
```
Ejemplo de ejecución
```
python3 ./ej4.py --input blast/nuc_orf0_2787.fas.xml --pattern homo --search
```

### Emboss 
Ejectuar distitos comandos de emboss
```
usage: ej5.py [-h] --input file.fas [--output filename] --method {orf_prot,orf_nt,translate,motifs,all}

Execute Emboss methods
  
  --input file.fas      input sequence file (.fas)
  --method {orf_prot,orf_nt,translate,motifs,all}
                        emboss method to execute: orf_prot finds ORF and saves them as protein sequences orf_nt saves them as nucleotide sequences translate translates sequence (.pep)
                        motifs executes domain analysis (.patmatmotifs)

optional arguments:
    -h, --help            show this help message and exit
  --output filename     path to save result
```
Ejemplo de ejecución
```
python3 ./ej5.py --input fasta/sequence.fas --method orf_prot --output test_prote
```
