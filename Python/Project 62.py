# project 62
import time
t0 = time.time()
result = dict()
for i in  range(10000):
    result[i]=''.join(sorted(str(i**3)))
l=[]
for i in  result.values():
    l.append(i)
res = []
for n,i in enumerate(l) :
    if l.count(i)==5:
        res.append(n**3)
print(min(res))
t1= time.time()
print(t1 - t0)


