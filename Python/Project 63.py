# project 63
import  math
c  = 0
for i in  range(1,10):
    for k in  range(1,22):
        if math.floor(1+k*math.log10(i))== k:
            c+=1
print(c)