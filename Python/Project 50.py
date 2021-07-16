# project 50

def is_prime(n):
    siven = [True]*n
    prime = []
    for i  in  range(2,n+1):
        if siven[i-1]:
            prime.append((i))
            siven[i*i-1::i] = [False]*len(range(i*i-1,n,i))
    return  prime

primes = is_prime(1000000)
length = 0

# value of the consecutive prime sum
largest = 0

# max value of the j variable(second for loop)
lastj = len(primes)

# two for loops
for i in range(len(primes)):
    for j in range(i+length, lastj):
        sol = sum(primes[i:j])
        if sol < 1000000:
            if sol in primes:
                length = j-i
                largest = sol
        else:
            lastj = j+1
            break
print(largest)




