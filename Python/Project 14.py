# project 14


def memo(f):
    f.cache = {}
    def _f(*args):
        if args not in f.cache:
            f.cache[args] = f(*args)
        return f.cache[args]
    return _f
@memo #<===== cache ram
def collatz(n):
    if n <= 1 : 
        return 1
    if n % 2 == 0 :
        return 1+collatz(n / 2)
    return 1+collatz(3 * n + 1)
print(max(range(1, 10**6), key=collatz))


