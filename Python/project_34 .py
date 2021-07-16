# project 34

from math import factorial as fact

if __name__ == '__main__':
    result =[]
    for i in range(3,1000000):
        s = sum(fact(int(l)) for l in str(i))
        if s == i:
            result.append(i)
    print(sum(result))
