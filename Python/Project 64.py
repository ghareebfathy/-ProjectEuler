# project 64
from math import sqrt
import time
start = time.time()
def continued_fraction(n):
    mn = 0.0
    dn = 1.0
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    period = 0
    if a0 != sqrt(n):
        while an != 2 * a0:
            mn = dn * an - mn
            dn = (n - mn ** 2) / dn
            an = int((a0 + mn)/dn)
            period += 1
    return period

counter = 0
for i in  range(10000):
    if continued_fraction(i)% 2== 1:
        counter+=1
print(counter)
end = time.time()
print( end - start)
