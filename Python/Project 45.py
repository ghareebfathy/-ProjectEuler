# project 45

def is_pentagonal(n):
	if (1+(24*n+1)**0.5) % 6 == 0:
		return True
	return False

result = 0
i = 143
while True:
	i+=1
	result = i * (2 * i - 1)
	if (is_pentagonal(result)):
		break
print(result)