# project 33

import math
def fractions():
	dp = 1
	np = 1
	for c in range(1,10):
		for  d in range(c):
			for n  in range(1,d):
				if (n * 10 + c) * d == (c * 10 + d) * n :
					np *= n
					dp *= d
	return dp / math.gcd(np,dp)
print(fractions())
