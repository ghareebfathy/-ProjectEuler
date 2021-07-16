# project 38


def Pandigital_num():
     r = int()
     for i in range(9000,10000):
          temp  = str(i)+str(i*2)
          if '0' not in temp :
               if len(set(temp)) == 9 :
                    if int(temp) > r :
                         r = int(temp)
     return r
print(Pandigital_num())
