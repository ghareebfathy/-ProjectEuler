# project 91
def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)

size= 50
reutlt = size * size * 3
for x in range(1,size+1):
    for y in range(1,size+1):
        fact = int(gcd(x,y))
        reutlt += min(y * fact // x ,(size - x)*fact //  y) * 2
print(reutlt)