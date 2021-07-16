# project 39

def intRightTri(n):
     
     result = 0
     resultSolutions = 0
     
     for p in range(2,n,2):
          numberOfSolutions = 0
          for a in range(2,p//3,2):
               if( p * (p - 2 * a ) % (2*(p-a)) == 0):
                    numberOfSolutions +=1
               if numberOfSolutions > resultSolutions:
                    resultSolutions = numberOfSolutions
                    result = p
     return result 
print(intRightTri(1000))
