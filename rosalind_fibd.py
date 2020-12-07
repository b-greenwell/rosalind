parameters_fh = open("./rosalind_fibd.txt",  'r')
parameters = parameters_fh.read()
parameters_fh.close()

##Create generational subroutine
def rabbits(a, b, c):
    return b + a - c


#parameters = "6 3"
para = parameters.split()
para = map(int, para)
(gen, lives) = para

##Starting information
arr = [[0, 1, 0, 1], [1, 0, 0, 1]]

##iterate over each generation, with recalculations for totals
for i in range(2, gen):
    newAdults = arr[i-1][0] + arr[i-1][1] - arr[i-1][2]
    newBuns = arr[i-1][0] - arr[i-1][2]
    if (i - lives >= 0):
        newDead = arr[i-lives][1]
    else:
        newDead = 0
    newTotal = newAdults + newBuns - newDead
    arr.append([newAdults, newBuns, newDead, newTotal])
    #print(newAdults, newBuns, newDead, newTotal)

print(arr[len(arr)-1][3])

##Example data I used to test
"""
1(s)
1
1 + 1(s) = 2
2 + 1(s) - 1 = 2
2 + 1(s) = 3
3 + 2(s) - 1 = 4

0 1 0 1
1 0 0 1
1 1 0 2
2 1 1 2
2 1 0 3
3 2 1 4
"""