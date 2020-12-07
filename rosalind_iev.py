#This exercise does not teach me much, so I will take shortcuts
import numpy as np
with open("./rosalind_iev.txt",  'r') as input:
    populations = input.readline().split()

##Convert populations to array
#populations = np.array([1, 0, 0, 1, 0, 1])
populations = list(map(int, populations))
populations = np.array(populations)
##How much each type of couple produces, from introductory genetics
scalars = np.array([2, 2, 2, 1.5, 1, 0])
print(sum(populations * scalars))