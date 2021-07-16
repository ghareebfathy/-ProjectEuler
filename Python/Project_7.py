# Problem 7

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
def prime_is_10001st__():
    count = 1
    l= []
    while True:
        if is_Prime_v3(count):
            l.append(count)
        if len(l) == 10001:
            break
        count += 1
    return l[-1]

print( prime_is_10001st__()) #  result  number : 104743
