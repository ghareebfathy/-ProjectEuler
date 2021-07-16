# project 22


def Problem_22():
     f = open('names.txt','r')
     char_num_dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
     names=sorted(f.read().replace('"','').strip('\n').split(','))
     sum_n=0
     for ind , value in enumerate(names):
          count = 0
          if '\n' not in value:
               for i in value:
                    count += char_num_dict[i]
          sum_n += count *(ind+1)
     f.close()
     return(sum_n) # result = 871198282
     
print(Problem_22())
