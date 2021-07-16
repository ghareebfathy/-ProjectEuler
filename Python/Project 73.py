# project 73
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


a = 3
b = 2
limit = 12000
result = 0
for d in  range(5,limit+1):
    for n in range(d//a+1,(d-1)//b+1):
        if gcd(n,d) == 1:
            result+=1
print(result)