from Bio import SeqIO
##Paired arrays of names and sequences
grphNames = []
grphSeq = []

for record in SeqIO.parse("./rosalind_lcsm.txt", "fasta"):
    grphNames.append(record.id)
    grphSeq.append(str(record.seq))

##Subroutine that generates all kmers of a given length in the given sequence
def generateKmers(seq, length):
    n = 0
    subseqs = {}
    while (n + length - 1 < len(seq)):
        subseqs[(seq[n:n+length])] = 1
        n = n + 1
    return list(subseqs.keys())

grphMax = max([len(seq) for seq in grphSeq])
seqMax = len(grphNames)
setDict = {}
##This is a computationally heavy way to do it
##Seed-growing would be better (probably)
##But I do not expect this script to take a while for Rosalind

##iterating over a length between 2 and the longest sequence + 1
for j in range(2, grphMax+1):
    subDict = {}
    ##we're going to add every possible kmer from every sequence
    ##to an array holding those as keys
    ##such that kmers that are shared will have a value greater than 1
    for i in range(len(grphNames)):
        #setDict = {}
        kmers = generateKmers(grphSeq[i], j)
        for kmer in kmers:
            subDict[kmer] = subDict.get(kmer, 0) + 1
    for kmer in list(subDict.keys()):
        if (subDict[kmer] < len(grphNames)):
            subDict.pop(kmer)
    if len(list(subDict.keys())) == 0:
        break
    setDict[j] = subDict
##Get the key (kmer) with the highest value
resMax = max(setDict.keys())
resSeq = ' '.join(list(setDict[resMax].keys()))
print(resSeq)
