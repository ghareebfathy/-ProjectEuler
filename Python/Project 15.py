# project 15

from math import factorial
def  pe15(n):
    return factorial(2 * n ) / factorial(n) / factorial(n)

print(pe15(20)) # 137846528820

"========================================================================="
def pe15_bis(num):
    ret = 1
    for j in range(1,num+1):
        ret *= num + j
        ret //= j
    return ret

print(pe15_bis(20)) # 137846528820
