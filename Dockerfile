FROM ubuntu:20.04

#run apt update
RUN apt-get update

#install pip wget
RUN apt-get install -y python3-pip wget

#install python dependencies
RUN pip3 install biopython

#change directory to /root
WORKDIR /root

#download muscle from github
RUN wget "https://github.com/rcedgar/muscle/releases/download/v5.1/muscle5.1.linux_intel64"

#move muscle to /usr/local/bin
RUN mv muscle5.1.linux_intel64 /usr/local/bin/muscle

#make muscle executable
RUN chmod +x /usr/local/bin/muscle

#download clustalw2
RUN wget "http://www.clustal.org/download/current/clustalw-2.1-linux-x86_64-libcppstatic.tar.gz"

#extract clustalw2
RUN tar -xvzf "clustalw-2.1-linux-x86_64-libcppstatic.tar.gz"

#move clustalw2 to /usr/local/bin
RUN mv clustalw-2.1-linux-x86_64-libcppstatic/clustalw2 /usr/local/bin/clustalw2


#download blast from ncbi
RUN wget "https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.13.0+-x64-linux.tar.gz"

#unzip blast
RUN tar -xvzf "ncbi-blast-2.13.0+-x64-linux.tar.gz"

#download blast db
RUN wget "https://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/swissprot.gz"

#unzip blast db
RUN gunzip "swissprot.gz"

#move blast to /usr/local/bin
RUN mv ncbi-blast-2.13.0+/bin/* /usr/local/bin/

#make blast db
RUN "makeblastdb" -in swissprot -dbtype prot