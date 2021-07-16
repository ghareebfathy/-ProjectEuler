

# Problem 5


import math
s = 21
def Smallest_multiple(n):
    global s
    for i in range(1,s):
        if n % i != 0:
            return False
    return True

number = s-1

while True:
	if Smallest_multiple(number):
		break
	number += s-1
    
print(number) #232792560
