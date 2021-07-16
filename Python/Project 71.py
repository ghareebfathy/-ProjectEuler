# project 71
a = 3
b = 7
r = 0
s = 1
limit = 1000000
for i in  range(limit,2,-1):
    p = (a * i - 1) // b
    if (p * s > r * i ):
        s = i
        r = p

print(r)