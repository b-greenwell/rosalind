from itertools import permutations
with open("./rosalind_perm.txt",  'r') as input:
    k = int(input.read())

#k = 3
perm = permutations(range(1, k + 1))
out = list(perm)
print(len(out))
for i in out:
    print(' '.join(map(str, list(i))))