import gzip
from Bio import SeqIO
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt

#unzip fastq file and store in recs
recs = SeqIO.parse(gzip.open('SRR003265.filt.fastq.gz','rt', encoding='utf-8'), 'fastq')
rec = next(recs)
# print(rec.seq)

#defaultdict(int) sets 0 as the default value
#count total for each nucleotide
cnt = defaultdict(int)
for rec in recs:
    for letter in rec.seq:
        cnt[letter] += 1

tot = sum(cnt.values())

# for letter, cnt in cnt.items():
#     print('%s: %.2f %d' % (letter, 100. * cnt / tot, cnt))

#N is a call in which a sequencer has detected an unknown base

n_cnt = defaultdict(int)
print(recs)
for rec in recs:
    print("HI")
    print(rec)
    for i, letter in enumerate(rec.seq):
        pos = i + 1
        print(letter)
        if letter == 'N':
            n_cnt[pos] += 1
            print(n_cnt)
    seq_len = max(n_cnt.keys(1))
    positions = range(1, seq_len + 1)
    fig, ax = plt.subplots(figsize=(16,9))
    ax.plot(positions, [n_cnt[x] for x in positions])
    ax.set_xlim(1, seq_len)
