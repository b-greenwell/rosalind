##Read in file
dna_fh = open("./rosalind_dna.txt",  'r')
dna = dna_fh.read()
dna_fh.close()
print(dna)

##Basic count and print
numA = dna.count('A')
numT = dna.count('T')
numC = dna.count('C')
numG = dna.count('G')
print("%s %s %s %s" % (numA, numC, numG, numT))

##These were NOT used, but people indicated them as potential answers:
##
print(*map(input().count, "ACGT"))
##
def qt(s):
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")
##
