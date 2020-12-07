##Read in initial constraints
import math
with open("./rosalind_lia.txt",  'r') as input:
    (k, N) = map(int, input.readline().split())

#(k, N) = [2, 1]
numInGen = 2**k

##Subroutine that handles the generational math
def binTheorem(N):
    p1 = math.factorial(numInGen) / (math.factorial(N) * math.factorial(numInGen - N))
    p2 = 0.25**N * 0.75**(numInGen - N)
    return(p1 * p2)

##Initialize at zero probability, add probability depending on generational math
prob = 0
for i in range(N, numInGen+1):
    prob += binTheorem(i)

print(prob)