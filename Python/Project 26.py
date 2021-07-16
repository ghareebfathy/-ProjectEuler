# project 26

def is_prime(R):
     sieve  = [True]*R
     primes = []
     for n in range(2,R+1):
          if sieve[n-1]:
               primes.append(n)# add numbert primes to convert number to string 
               sieve[n*n-1::n] = [False]*len(range(n*n-1,R,n))
     return primes

def f(N):
    if N < 8: return 3
    for d in is_prime(N)[::-1]:
        k = d//2
        while pow(10, k, d) != 1: 
          k+= 1
        if d-1 == k: return d
print(f(1000))

