##Read in entire codon table
codonTable = {}
with open("./rosalind_prot_table.txt",  'r') as codonTableFH:
    for line in codonTableFH:
        (codon, AA) = line.split()
        codonTable[codon] = AA

##Also read in nucleotide sequence of interest
#prot = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
prot_fh = open("./rosalind_prot.txt",  'r')
prot = prot_fh.read()
prot_fh.close()

##From StackOverflow, split every 3 characters
prot = [prot[i:i+3] for i in range(0, len(prot), 3)]
##and then convert the 3 characters (codon) to an amino acid
prot2 = [codonTable.get(key) for key in prot]
print(''.join(prot2[0:len(prot2)-2]))