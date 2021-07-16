#Largest palindrome product
#Problem 4


def palindrome_num(n):
    sring_number = str(n)
    return sring_number == sring_number[::-1]

reslut =[]
for i in range(100,999):
    for j in range(100,999):
        m = i * j
        if palindrome_num(m):
            reslut.append(m)
print(max(reslut)) #Answer:  906609

# def is_palindrome(num):
#     # Skip single-digit inputs
#     if num // 10 == 0:
#         return False
#     temp = num
#     reversed_num = 0

#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10

#     if num == reversed_num:
#         return num
#     else:
#         return False


 
# result = 0

# for i in range(99999,99,-11):
# 	for j in range(99999,99,-1):
# 		m = i * j
# 		if m < result:
# 			break
# 		if palindrome_num(m):
# 			result = m
# 			break



