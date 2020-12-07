from Bio import SeqIO
import regex as re
for record in SeqIO.parse("./rosalind_orf.txt", "fasta"):
    seq = record.seq

#There are probably easier and more efficient ways to do this
#But I will discover those later
possibleSeqs = {}
seqRev = seq.reverse_complement()
##Take all ORFs in DNA
ORFs = [seq, seq[1:], seq[2:], seqRev, seqRev[1:], seqRev[2:]]
for i in range(6):
    iSeq = ORFs[i]
    ##removing any trailing nucleotides
    trailing = len(str(iSeq)) % 3
    if (trailing > 0):
        iSeq = iSeq[:-trailing]
    ##Convert to amino acid
    asAA = str(iSeq.translate())
    ##Regex match an ORF, because all of them will start with M and end with *
    ##This regex has to be not-greedy (lazy?) though, as the first * it encounters is the end
    for match in re.findall("M[^\*]*\*", asAA, overlapped=True):
        possibleSeqs[match] = i

for key in possibleSeqs.keys():
    print(key[:-1])