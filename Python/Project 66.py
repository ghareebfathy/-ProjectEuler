# project 66
import math
result = 0
pmax = 0
for i in  range(2,1000):
    limit = int(math.sqrt(i))
    if limit * limit == i:continue
    m = 0
    d = 1
    a = limit
    num1 = 1
    num = a
    denm1 = 0
    den = 1
    while (num * num - i * den * den != 1):
        m = d * a - m
        d = (i - m * m) // d
        a = (limit + m) // d
        numm2 = num1
        num1 = num
        denm2  = denm1
        denm1 = den
        num = a * num1 + numm2
        den = a * denm1 + denm2
    if num > pmax:
        pmax = num
        result = i
print(result)