# project 16
# Power digit sum


def Power_digit_sum(n):
	number = list(str(2**n))
	result= [int(i) for i in number]
	return sum(result)

print(Power_digit_sum(15)) # result 26

print(Power_digit_sum(1000)) # result 1366



