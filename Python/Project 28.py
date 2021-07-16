# project 28

def Number_spiral_diagonals(n):
     n = (n -1)/2
     return 2 * n * (8 * n * n + 15 * n + 13) / 3 + 1
print(Number_spiral_diagonals(1001)) # result 669171001.0


# or

def Number_spiral_diagonals2(n): # speed code
     return (n * (n * (4 * n + 3) + 8)-9) /6
print(Number_spiral_diagonals2(1001)) # result 669171001.0
