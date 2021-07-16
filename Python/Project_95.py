# project 95
def findchains(limit=1000000):
	divsum = [0]*limit
	for n in range(1, limit//2):
		for i in range(2*n, limit, n):
			divsum[i] += n

	chains = []
	for n in range(2, limit):
		chain = []
		while 1 < divsum[n] < limit:
			chain.append(n)
			divsum[n], n = -divsum[n], divsum[n]

		if -divsum[n] in chain:
			chain = chain[chain.index(n):]
			start = chain.index(min(chain))
			chain = chain[start:] + chain[:start]
			chains.append(chain)
	

	for i in chains:
		for j in i :
			if j > 12496 :
				return j
print(findchains())
