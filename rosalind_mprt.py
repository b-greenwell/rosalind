#First time working with URLs AND file paths AND regex in python
#So I'm not sure that I did the file name creation the *best* way (I did it as if it was R),
# but it works for a first attempt
import os
import regex as re
from Bio import SeqIO
import urllib.request

##Read important uniprot IDs
uniprotIDs = []
with open("./rosalind_mprt.txt",  'r') as input:
    uniprotIDs = input.read().splitlines()

print(uniprotIDs)
#uniprotIDs = ["A2Z669", "B5ZC00", "P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]

##Download (or find already) the right uniprot IDs
for id in uniprotIDs:
    filepath = ''.join(["./", id, ".fasta"])
    print(filepath)
    if (os.path.isfile(filepath)):
        ##File found already, no need to download
        pass
    else:
        ##Otherwise download it
        urlpath = ''.join(["https://www.uniprot.org/uniprot/", id, ".fasta"])
        urllib.request.urlretrieve(urlpath, filepath)

##Gather all file paths into one array
uniprotFastas = [''.join(["./", id, ".fasta"]) for id in uniprotIDs]

##Glycosylation motif we're looking for
match_string = "N[^P][ST][^P]"
for i in range(len(uniprotIDs)):
    id = uniprotIDs[i]
    nMatches = []
    for record in SeqIO.parse(uniprotFastas[i], "fasta"):
        ##if we find the motif, put it in nMatches
        seq = str(record.seq)
        for match in re.findall(match_string, seq, overlapped = True):
            nMatches.append(seq.find(match)+1)
    ##Print out all matches, joined by a space
    if len(nMatches) > 0:
        print(id, "\n", ' '.join(map(str, nMatches)))