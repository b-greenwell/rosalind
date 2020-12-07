##There are ways to read in a fasta file in base, but let's not re-invent the wheel
from Bio import SeqIO
gc_dict = {}

##Counting G+C nucleotides, return as %
def GC(seq):
    gcCounts = seq.count("C") + seq.count("G")
    dnaLength = len(seq)
    return(100 * gcCounts/dnaLength)

##Record the GC% of every fasta entry
for record in SeqIO.parse("./rosalind_gc.txt", "fasta"):
    gc_dict[record.id] = GC(record.seq)

##Print the key for the highest value, from a helpful StackOverflow
max_key = max(gc_dict, key = gc_dict.get)
print(max_key, "\n", gc_dict[max_key])