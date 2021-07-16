# Problem 116
n=50
def f(m,n):
    result = [1] * m + [0] * (n - m + 1)
    for j in range(m, n + 1):
        result[j] += result[j - 1]+result[j - m]
    return result[n] - 1
print(f(2,n) + f(3,n) + f(4,n))
count = 0
m=2
while m <= 4:
    count += f(m,n)
    m += 1
print(count)



def fv(n):
  sum = 0
  k = 1
  while k <= n:
      if k % 2 == 1:
          sum = sum + 1.0/k
      else:
          sum = sum - 1.0/k
      k = k + 1
  return sum
print(fv(1260))