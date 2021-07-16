# project 46

import math
def is_prime(x):
    if x <= 1:
        return False
    if x == 2 :return True
    if x > 2 and x % 2 == 0:
        return False
    sqrt_num = math.floor(math.sqrt(x))
    for i in range(3,sqrt_num+1,2):
        if x % i == 0:
            return False
    return True




# iterator
number = 3

# list of primes
primes = [2]


# while loop

while True:
    if is_prime(number):
        primes.append(number)
    else:
        for i in primes:
            if math.sqrt(((number-i)/2)) == int(math.sqrt(((number-i)/2))):
                break
        else:
            print (number)
            break

    number += 2
