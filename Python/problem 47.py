# project 47

def prime_number(R):
    # prime numbers
    sieve  = [True]*R
    prime = set()
    for n in range(2,R+1):
        if sieve[n-1]:
            prime.add(n)# add numbert primes to convert number to string
            sieve[n*n-1::n] = [False]*len(range(n*n-1,R,n))
    return prime
primes = list(prime_number(10000)) # list prime


def chack(n,prime): # creates a list of prime factors
    factors = []
    for i in  range(0,len(prime)):
        if n % prime[i] ==0:
            factors.append(prime[i])
    return factors

#
for i in range(0,1000000):
    list = chack(i,primes)
    if len(list)==4:
        list = chack(i+1,primes)
        if len(list)==4:
            list = chack(i + 2, primes)
        if len(list) == 4:
            list = chack(i + 3, primes)
        if len(list) == 4:
                list = chack(i + 4, primes)
                print(i) # result 134043
                break
