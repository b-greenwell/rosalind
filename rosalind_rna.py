rna_fh = open("./rosalind_rna.txt",  'r')
rna = rna_fh.read()
rna_fh.close()

#rna = "ACGT"
##Swap T for U
rna = rna.translate(str.maketrans("T", "U"))
print(rna)