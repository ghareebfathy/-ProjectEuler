# project 27

import math
def isPrime(x):
    # invalid input
    if x <= 1:
        return False
    if x == 2 :return True
    if x > 2 and x % 2 == 0:
        return False
    sqrt_num = math.floor(math.sqrt(x))
    for i in range(3,sqrt_num+1,2):
        if x % i == 0:
            return False
    return True


# upper and lower limit
# change the value of limit according to your value
value = 1000
# make sure it's a positive number
if value < 0:
    value = -value

# number of generated primes of the best sequence
count = 0
# its coefficients
value_a = 0
value_b = 0

# Apply brute-force
for a in range(-value, value):
    for b in range(-value, value):

        # count of consecutive prime numbers
        l = 0
        while isPrime(l * l + a * l + b):
            l += 1

        if count < l:
            count = l
            value_a = a
            value_b = b

print("Product value =", (value_a * value_b))
print("a:", value_a, "b:", value_b)
# Product value = -59231
# a: -61 b: 971