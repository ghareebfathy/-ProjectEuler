# project 49

from  itertools import  permutations
def number_prime(n):
    siven = [True]*n
    prime = []
    for i  in  range(2,n+1):
        if siven[i-1]:
            prime.append(i)
            siven[i*i-1::i] = [False]*len(range(i*i-1,n,i))
    return  prime

# create the number
def create(b):
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            difference = b[j] - b[i]
            if b[j] + difference in b:
                return str(b[i])+str(b[j])+str(b[j]+difference)
    return False

# sieving prime numbers less than 10000
result = (number_prime(10000))
# primes greater than 1487
primes = [x for x in  result if x > 1487]
# for loop
for i  in primes:
    p = permutations(str(i))
    a = [int (''.join(x))for  x in p]
    a = list(set([x for  x in a if x in primes]))
    a.sort()
    if len(a) >= 3:
        if create(a):
            print(create(a))
            break




