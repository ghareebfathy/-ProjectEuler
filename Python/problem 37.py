# project 37


import time
t1 = time.time()
# chack prime

R      = 1000000
sieve  = [True]*R
primes = set()
for n in range(2,R+1):
    if sieve[n-1]:
        primes.add(str(n))# add numbert primes to convert number to string 
        sieve[n*n-1::n] = [False]*len(range(n*n-1,R,n))

#Truncatable primes

truncable = []
for p in primes:
    if len(p) == 1: continue
    if all(p[:i] in primes and p[i:] in primes for i in range(1,len(p))):
        truncable.append(int(p))

print(sum(truncable))
t2 = time.time()
print(t1 - t2)




