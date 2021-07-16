# project 53

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
limit = 1000000
nilimit = 100
result = 0
for n in  range(1,nilimit+1):
    for r in  range(n):
        if factorial(n) / (factorial(r)*factorial(n-r))>= limit:
            result += 1
print(result)