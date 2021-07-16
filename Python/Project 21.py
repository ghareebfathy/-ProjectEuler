# project 21

from functools import lru_cache

@lru_cache(maxsize=1000)
def amicable_numbers(x):
     sum1 = sum([i for i in range(1,x)if x % i == 0 ])
     sum2 = sum([j for j in range(1,sum1)if sum1 % j == 0])
     return x  == sum2 and sum1 != sum2
     

l =0
for i in range(1,10000):
     if(amicable_numbers(i)):
          l+=(i)

print(l)#31626
