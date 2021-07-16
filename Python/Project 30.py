# project 30

def digit_power():
    return sum(i for i in range(10,1000000)if i == sum(int(d)** 5 for d in str(i)))

print(digit_power()) # 443839
