# project 56

def power_number(n):
    for num in  range(n):
        for power in  range(n):
            yield num ** power

def get_digital_sum(n):
    return sum(int(d) for d in str(n))

def max_sum(n):
    return  max(get_digital_sum(num) for num in power_number(n))
print(max_sum(100))

print(max(sum(map(int, str(a**b))) for a in range(100) for b in range(100))) # smpli code

