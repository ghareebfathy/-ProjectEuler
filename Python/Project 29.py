# project 29

def Distinct_powers(n):
    list_num =[]
    count = 2
    while count <= n :
        for i in range(2,n+1):
            list_num.append(count ** i)
        count += 1
    return len(set(list_num))
print(Distinct_powers(100))
