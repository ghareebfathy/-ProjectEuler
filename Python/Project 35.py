# project 35

import math 
def is_circular_prime(number):
    number = str(number)
    i = remainder = value = total = 0
    digits = len(number)
    num = int(number)
    # Here we will pick the last digit and
    # place it at the start in order to form
    # a new rotation.
    # 199 -> 919 -> 991    
    while i < digits:
        # Dividing the number in digits
        # 199 % 10 = 9(last digit)
        remainder = int(num % 10)
        num = int(num / 10)
        num = int((remainder * (10 ** (digits - 1)) + num))
        value = is_prime(num)
        total += value
        i += 1
    if total is digits:
        return True
    return False

# Function to check number is a prime or not
def is_prime(n):
     if n <= 1 :return False
     if n == 2 : return True
     if n > 2 and n % 2 == 0:return False
     sqrt_num = math.floor(math.sqrt(n))
     for i in range(3,1+sqrt_num,2):
          if n % i == 0: return False
     return True

# Driver Function
l = []
for i in range(1000000):
     if is_circular_prime(i):
          l.append(i)
print(len(l))# result 55