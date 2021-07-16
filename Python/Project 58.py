# project 58

import math
def is_prime(n):
    if n == 1:return False
    if n == 2 : return True
    if n > 2 and n % 2 == 0:
        return False
    sqrt_num = math.floor(math.sqrt(n))
    for i in range(3,sqrt_num+1,2):
        if n % i == 0 :
            return False
    return True



noofprime = 3
sl = 2
c = 9
while ((noofprime) / (2 * sl +1)> 0.10):
    sl += 2
    for i in  range(3):
        c += sl
        if is_prime(c):
            noofprime+=1
    c+=sl

print(sl+1) # result 26241