# project 76
ways = [0]*101
ways[0] = 1
for x in range(1,100):
    for i in range(x, 101):
        ways[i] += ways[i-x]
print (ways[100])
