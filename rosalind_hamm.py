##Read in file
hamm_fh = open("./rosalind_hamm.txt",  'r')
hamm = hamm_fh.read()
hamm_fh.close()

##Compare characters in hamm1 vs hamm2
##There is probably a much easier/elegant way of doing this, but for now here goes
hamm = hamm.split("\n")
hamm1 = list(hamm[0])
hamm2 = list(hamm[1])
n = 0
for i in range(len(hamm[0])):
    if hamm1[i] != hamm2[i]:
        n = n + 1
print(n)