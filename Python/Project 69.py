# project 69
def primes(R):

    sieve  = [True]*R
    primes = list()
    for n in range(2,R+1):
        if sieve[n-1]:
            primes.append(n)# add numbert primes to convert number to string
            sieve[n*n-1::n] = [False]*len(range(n*n-1,R,n))
    return primes

p = (primes(200))


from sympy.ntheory.factor_ import totient

result = 1
i = 0
limit = 1e6
while (result * p[i] < limit):

    result *= p[i]

    i+=1
print(result)
