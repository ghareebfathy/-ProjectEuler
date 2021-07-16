# project 99
"pow numbers is largest exponential "
from  time import time
from  math import log10
t0 = time()

file = open('p099_base_exp.txt','r')
l = [0,0]

for i,f in enumerate(file) :
    a,x = list(map(int,f.split(',')))
    if x * log10(a) > l[0]:
        l = [x * log10(a),i+1]

print(l)

t1 = time()
print('this time',t0 - t1)