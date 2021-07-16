# Problem 2

def evenFibSum(limit) : 
     if (limit < 2) : 
        return 0
     ef1 = 0
     ef2 = 2 
     sm = ef1 + ef2
     while (ef2 <= limit):
          ef3 = 4 * ef2 + ef1
          if (ef3 > limit):
               break
          ef1 = ef2
          ef2 = ef3
          sm += ef2
     return sm
print(evenFibSum(4e6))


def evenFibSum(n) :
	a ,b = 1 , 2
	s = 0
	t = 0
	while (a<= n):
		t = a
		a = b
		b+=t
		if (t % 2 == 0):
			s+=t
	return s
print(evenFibSum(4e6))
'==============================================='


fibonacci_cache = {}
def fibonacci(n):
     if n in fibonacci_cache :
          return fibonacci_cache[n]
     if n == 1 :
          value = 1
     elif n == 2 :
          value = 2
     elif n > 2 :
          value = fibonacci(n-1) + fibonacci(n-2)
     fibonacci_cache[n] = value
     return value
result = []
for i in range(1,100):
     result.append(fibonacci(i))
sum_num =[]
for i in result:
     if i % 2 == 0:
          sum_num.append(i)
     if i > 4e6:
          break
print(sum(sum_num))