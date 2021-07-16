# Problem 10
# Summation of primes

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""
import math
def primes(n):
     if n == 1 :
          return False
     if n == 2:
          return True
     if n > 2 and n % 2 == 0 :
          return False
     sqrt_n = math.floor(math.sqrt(n))
     for i in range(3,1+sqrt_n,2):
          if n % i == 0:
               return False
     return True
sum_tow_million = 0
for i in range(2000000):
     if primes(i):
          sum_tow_million += i
print(sum_tow_million) # result ==> 142913828922
