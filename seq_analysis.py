from Bio import Entrez, SeqIO, Seq
from Bio.Alphabet import IUPAC

#retrieve sequence from Entrez and save to fasta file
Entrez.email = "jesse.sosnicki@gmail.com"
handle = Entrez.efetch(db='nucleotide', id=['NM_002299'], rettype='fasta') #Lactase Gene
seq = SeqIO.read(handle, 'fasta')
w_hdl = open('example.fasta', 'w')
w_seq = seq[11:5795]
SeqIO.write([w_seq], w_hdl, 'fasta')
w_hdl.close()

#print details of the FASTA file
recs = SeqIO.parse('example.fasta', 'fasta')
for rec in recs:
    seq = rec.seq
    # print(rec)

s = Seq.Seq(str(seq), IUPAC.unambiguous_dna)
rna = s.transcribe()
# print(rna)

prot = seq.translate()
print(prot)