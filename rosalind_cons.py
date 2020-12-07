#Not going to re-invent the wheel as far as input
#There's probably a consensusMatrix option for Biopython like in Bioconductor,
#but I feel like that wouldn't help learn this lesson
from Bio import SeqIO
import numpy as np

cons = []
for record in SeqIO.parse("./rosalind_cons.txt", "fasta"):
    cons.append(list(record.seq))

##Return an array of nucleotide counts in order ACGT
def countNucs(s):
    return [s.count("A"), s.count("C"), s.count("G"), s.count("T")]

##Get number rows and columns
consArr = np.array(cons)
nRow, nCol = consArr.shape

##Count nucleotides by position
nucCounts = []
for i in range(nCol):
    nucCounts.append(countNucs(list(consArr[0:nRow, i])))

##Get index of max (A, C, G, T)
consSeqList = []
for i in range(0, nCol):
    maxIndex = nucCounts[i].index(max(nucCounts[i]))
    consSeqList.append(maxIndex)
##Convert index to nucleotide
consSeq = ''.join(map(str, consSeqList))
consSeq = consSeq.translate(str.maketrans("0123", 'ACGT'))

nucOrder = ['A', 'C', 'G', 'T']
print(consSeq)
##Print final nucleotide count in order ACGT, separated by spaces
for i in range(4):
    print(nucOrder[i] + ':', ' '.join(map(str, [item[i] for item in nucCounts])))


