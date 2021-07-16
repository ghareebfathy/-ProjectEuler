# project 40

def Champernownes():
	a = ''
	for i in range(1,1000000):
		a += str(i)
	d1 = int(a[0])
	d10 = int(a[9])
	d100 = int(a[99])
	d1000 = int(a[1000-1])
	d10000 = int(a[10000-1])
	d100000 = int(a[100000-1])
	d1000000 = int(a[1000000-1])
	return d1*d10*d100*d1000*d10000*d100000*d1000000

print(Champernownes())
