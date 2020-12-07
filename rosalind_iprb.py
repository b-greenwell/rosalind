import numpy
parameters_fh = open("./rosalind_iprb.txt",  'r')
parameters = parameters_fh.read()
parameters_fh.close()

##Convert parameters to initial population and probabilities
#parameters = "2 2 2"
para = parameters.split()
para = map(int, para)
(aa, ab, bb) = para
population = aa + ab + bb
initialPops = numpy.array([aa, ab, bb])
initialProbs = initialPops/population

##I'll be honest, hardcoding the predetermined genomic values did not feel like a pretty way to do it
total = 0
for i in range(3):
    ##i is first allele
    probChosen1 = initialProbs[i]
    newPops = initialPops.copy()
    newPops[i] = newPops[i] - 1
    newTotal = population - 1
    newProbs = newPops/newTotal
    for j in range(3):
        ##j is second allele
        outcome = 0
        if (i == 0):
            outcome = 1
        elif (i == 1):
            outcome = newProbs[0] * 1 + newProbs[1] * 0.75 + newProbs[2] * 0.5
        else:
            outcome = newProbs[0] * 1 + newProbs[1] * 0.5
        total = total + probChosen1 * outcome
print(total/3)
