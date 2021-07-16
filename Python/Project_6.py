# Problem 6

def Sum_square_difference():
    res ,x = 0 , 0
    for i in range(1,101):
        res += i * i
        x += i
    return (x * x) - res

print(Sum_square_difference())
        
        
    

N = 100
sum_n = N * (N+1)/2
squared= (N * (N + 1)*(2*N+1))/6
result = sum_n * sum_n - squared
print(int(result))
