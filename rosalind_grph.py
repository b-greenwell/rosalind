from Bio import SeqIO
##Create paired arrays to hold names and sequences
##Maybe there's a better way to do this in python? Tuples?
grphNames = []
grphSeq = []

##Add name and sequence to respective arrays
for record in SeqIO.parse("./rosalind_grph.txt", "fasta"):
    grphNames.append(record.id)
    grphSeq.append(record.seq)

##Get first 3nt and last 3nt for each record
starts = [seq[0:3] for seq in grphSeq]
ends = [seq[-3:] for seq in grphSeq]
##Shotgun approach, compare all starts to all ends
for i in range(len(grphNames)):
    for j in range(len(grphNames)):
        ##Skip if they come from the same sequence
        if (starts[i] == ends[j] and i != j):
            print(grphNames[j], grphNames[i])
