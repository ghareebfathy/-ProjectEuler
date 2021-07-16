# project 20

# Factorial digit sum

def memo(f):
    f.cache = {}
    def _f(*args):
        if args not in f.cache:
            f.cache[args] = f(*args)
        return f.cache[args]
    return _f
@memo #<===== cache ram
def digit_sum(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    list_num = list(str(res))
    return sum([int(i) for i in list_num])

print(digit_sum(100)) # 648
