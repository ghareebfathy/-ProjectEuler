# project 32
    
def isPandigital(Str):

	if (len(Str) != 9):
		return bool(False)

	ch = "".join(sorted(Str))

	if (ch == "123456789"):
		return bool(True)
	else:
		return bool(False)

def PandigitalProduct_1_9(n): 
	i = 1
	while i * i <= n:
		if ((n % i == 0) and
			bool(isPandigital(str(n) +str(i) +str(n // i)))):
			return bool(True)	
		i += 1
	return bool(False)

result = []
count = 0
for i in range(123456789):
    if PandigitalProduct_1_9(i):
        result.append(i)
        count+=1
        if count == 7:
            break
print('Don !')
print(sum(result)) # result ===> 45228
