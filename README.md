# Bioinformatica 

## Análisis de Retinblastoma Gen RB1

### Integrantes 
- Corfdir, Yohann                     
- Jerusalinsky, Agustín	 
- Piñeiro, Eugenia Sol		 
- Quesada, Francisco 

### Requerimientos 
```
Python3 
Clustawl
Muscle
Blast 
```
Para instalar los modulos de Python necesarios ejectuar el siguiente comando:
```
pip install requeriments.txt
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
python3 ./ej2.py --input multiple.fas 
```

### MSA

Para ejectuar Multiple Sequence Alignment con Muscle ejecutar:
```
python3 ./ej3.py --algorithm muscle 
```
Para ejectuar Multiple Sequence Alignment con Clustawl ejecutar
```
python3 ./ej3.py --algorithm clustawl 
```
