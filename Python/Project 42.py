# project 42

import time
t0 = time.time()
def isTriangular(num):
	if (num < 0):
		return False
	sum, n = 0, 1

	while(sum <= num): 
	
		sum = sum + n
		if (sum == num):
			return True
		n += 1
	return False

def Problem_42():
	f = open('p042_words.txt','r')
	char_num_dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
	names=sorted(f.read().replace('"','').strip('\n').split(','))
	count = 0
	for value in (names):
		s = sum([char_num_dict[i] for i in value])
		if isTriangular(s):
			count +=1
		f.close()
	return  count

print(Problem_42())


t1 = time.time()
print(t0 - t1)
