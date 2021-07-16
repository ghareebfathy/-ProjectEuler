# Problem 3

import math
def is_Prime_v3(x):
    if x == 1 :
        return False
    if x == 2 :
        return True
    if x > 2 and   x % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(x))
    for d in range(3,1+max_divisor,2):
        if x % d == 0:
            return False
    return True


#for i in range(1,600851475143):
	#if is_Prime_v3(i)  == True:
		#if 600851475143 % i == 0:
			#pass #print(i)
"""
71
839
1471
6857
<====
"""
def largeest_prime(n):
    factor = 2
    while factor ** 2 <= n:
        if n % factor == 0:
            print(n, '/ %s' % factor)
            n //= factor
        else:
            if factor == 2 :
                factor = 3
            else:
                factor += 2
    if n > factor :
        return n


print(largeest_prime(13195))
print('---------------------')
print(largeest_prime(600851475143))
