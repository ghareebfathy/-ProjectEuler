# project 77
import time
t0 = time.time()
def primes(R):

    sieve  = [True]*R
    primes = list()
    for n in range(2,R+1):
        if sieve[n-1]:
            primes.append(n)# add numbert primes to convert number to string
            sieve[n*n-1::n] = [False]*len(range(n*n-1,R,n))
    return primes
target = 2
p=(primes(1000))
while True:
    ways = [0]*5001
    ways[0] = 1
    for x in  p:
        for i in range(x, 5000):
            ways[i] += ways[i-x]
    if (ways[target] > 5000):break
    target+=1
t1 = time.time()
print(target)
print(t0 - t1)