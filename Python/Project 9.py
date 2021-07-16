# Problem 9
# Special Pythagorean triplet

def euler9():
    p = 1000
    for a in range(1, p+1):
        for b in range(a + 1, a+p+1):
            c = p - a - b
            if a ** 2 + b ** 2 == c**2:
                 print(a*b*c)
                 return
euler9() # 31875000
