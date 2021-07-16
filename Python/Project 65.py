# project 65
def digitsum(n):
    return  sum([int(digit)for digit in str(n)])
d =1
n = 2
for i in  range(2,100):
    temp = d
    if i % 3 == 0:
        c = 2 * (i // 3)-2
    else:
        c = 1
    d = n
    n = c * d + temp
print(digitsum(n))