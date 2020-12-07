##Read in sequence as string
subs_fh = open("./rosalind_subs.txt",  'r')
subs = subs_fh.read()
subs_fh.close()
(string, sub, na) = subs.split("\n")

#(string, sub) = ["GATATATGCATATACTT", "ATAT"]
##i + 1 to convert from indices to positions
##Find all positions that match and print
res = [i+1 for i in range(len(string)) if string.startswith(sub, i)]
print(' '.join(map(str, res)))
