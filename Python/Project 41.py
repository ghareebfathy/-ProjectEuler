# project 41

import math
from itertools import permutations

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
p = list(permutations ('7654321'))
count = []
l =[]
for i in p:
    if is_Prime_v3((int(''.join(i)))):
        l.append(int(''.join(i)))
print(max(l))# 7652413