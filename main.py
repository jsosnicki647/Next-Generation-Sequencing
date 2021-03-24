#access the Entrez database
from Bio import Entrez, Medline, SeqIO
Entrez.email = "jesse.sosnicki@gmail.com" 

#retrieve the list of databases from Entrez
handle = Entrez.einfo()
rec = Entrez.read(handle)
# print(rec)

#search nucleotide database for the CRT gene and the Plasmodium falciparum organism
handle = Entrez.esearch(db="nucleotide", term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]')
rec_list = Entrez.read(handle)
print(rec_list)
print(int(rec_list['RetMax']) < int(rec_list['Count']))
if int(rec_list['RetMax']) < int(rec_list['Count']):
    handle = Entrez.esearch(db="nucleotide", term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]',
                            retmax=rec_list['Count'])
    rec_list = Entrez.read(handle)
print(rec_list)