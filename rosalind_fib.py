parameters_fh = open("./rosalind_fib.txt",  'r')
parameters = parameters_fh.read()
parameters_fh.close()

##Create subroutine for each generation
def rabbits(a, b):
    return  b + a * 3

#parameters = "5 3"
para = parameters.split()
para = map(int, para)
(gen, offspring) = para
#Hardcoding the first entry like this is not the most elegant solution
arr = [1, 1]

##Iterate over each generation, adding the result to the end of the array
for i in range(2, gen):
    arr.append(rabbits(arr[i - 2], arr[i - 1]))
print(max(arr))