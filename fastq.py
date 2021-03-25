import gzip
from Bio import SeqIO
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt

recs = SeqIO.parse(gzip.open('SRR003265.filt.fastq.gz','rt', encoding='utf-8'), 'fastq')
rec = next(recs)
print(rec.id, rec.description, rec.seq)
print(rec.letter_annotations)

cnt = defaultdict(int)

for rec in recs:
    for letter in rec.seq:
        cnt[letter] += 1

tot = sum(cnt.values())

for letter, cnt in cnt.items():
    print('%s: %.2f %d' % (letter, 100. * cnt / tot, cnt))

n_cnt = defaultdict(int)
for rec in recs:
    for i, letter in enumerate(rec.seq):
        pos = i + 1
        if letter == 'N':
            n_cnt[pos] += 1
    seq_len = max(n_cnt.keys(1))
    positions = range(1, seq_len + 1)
    fig, ax = plt.subplots(figsize=(16,9))
    ax.plot(positions, [n_cnt[x] for x in positions])
    ax.set_xlim(1, seq_len)
