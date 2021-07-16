# Problem 1

def Multiples(n,m):
    total_sum = 0
    for i in range(1000):
        if (i % n == 0 or i % m == 0 ):
            total_sum += i
    return total_sum

print(Multiples(5,3))

def Multiples2(n,m):
	return sum([i for i in range(1000) if i % n == 0 or i % m == 0])

print(Multiples2(5,3))


def numbers(n,m,final_number):
	last_mul_3 = (final_number - 1 ) // 3
	last_mul_5 = (final_number - 1 ) // 5
	last_mul_15 = (final_number - 1 ) // 15
	sum_3 = 3 * (last_mul_3 / 2 ) * (1 + last_mul_3)
	sum_5= 5 * (last_mul_5 / 2 ) * (1 + last_mul_5)
	sum_15= 15 * (last_mul_15 / 2 ) * (1 + last_mul_15)
	return sum_3 + sum_5 - sum_15

numbers(3,5,1000000000000)
