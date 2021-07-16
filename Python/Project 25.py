# project 25

from functools import lru_cache

@lru_cache(maxsize=5000)
def fibonacci(n):
    if n == 1 : return 1
    elif n == 2 : return 1
    elif n > 2 :

        return fibonacci(n - 1) + fibonacci(n - 2)



c = 0
while True :
	m = str(fibonacci(c))
	if len(m) == 1000:
		break
	c+=1
print(c) # reslut 4782
