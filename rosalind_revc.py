rna_fh = open("./rosalind_revc.txt",  'r')
rna = rna_fh.read()
rna_fh.close()

##Complement then reverse
rna = rna.translate(str.maketrans('ACGT', 'TGCA'))
rna = list(rna)
rna.reverse()
revc = ''.join(rna)
print(revc)