#access the Entrez database
from Bio import Entrez, Medline, SeqIO
Entrez.email = "jesse.sosnicki@gmail.com" 

#retrieve the list of databases from Entrez
handle = Entrez.einfo()
rec = Entrez.read(handle)

#search nucleotide database for the CRT gene and the Plasmodium falciparum organism
handle = Entrez.esearch(db="nucleotide", term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]')
rec_list = Entrez.read(handle)

#if the count is hire then the RetMax, set RetMax attribute equal to the count and search again
if int(rec_list['RetMax']) < int(rec_list['Count']):
    handle = Entrez.esearch(db="nucleotide", term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]',
                            retmax=rec_list['Count'])
    rec_list = Entrez.read(handle)

#store the IDs returned by Entrez to a new list
id_list = rec_list['IdList']

handle = Entrez.efetch(db='nucleotide', id=id_list, rettype='gb')
recs = list(SeqIO.parse(handle, 'gb'))

#search for a specific record 'KM288867'
for rec in recs:
    if rec.name == 'KM288867':
        break

#extract features from rec and print
for feature in rec.features:
    if feature.type == 'gene':
        print('GENE\n%s' % feature.qualifiers['gene'])
    elif feature.type == 'exon':
        loc = feature.location
        print('EXON\n%s' % loc.start, loc.end, loc.strand)
    else:
        print('not processed:\n%s' % feature)

print(rec.seq)