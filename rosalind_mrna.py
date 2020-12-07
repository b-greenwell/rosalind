#How many codons code for each result?
codonTableRev = {}
with open("./rosalind_prot_table.txt",  'r') as codonTableFH:
    for line in codonTableFH:
        (codon, AA) = line.split()
        codonTableRev[AA] = codonTableRev.get(AA, 0) + 1

##Subroutine for product of all inputs
def product(l):
    total = 1
    for x in l: total = total * x
    return total


with open("./rosalind_mrna.txt",  'r') as input:
    seq = input.readline().rstrip()

##Read in the sequence, multiply all inputs together
#seq = "MA"
seqList = list(seq)
seqList.append("Stop")
seqMatch = [codonTableRev[AA] for AA in seqList]
seqTotal = product(seqMatch)
##The directions ask to run mod 1E6 on the result... so let's just take the last 6 digits as a shortcut
SeqMod = str(seqTotal)[-6:]
print(SeqMod)
